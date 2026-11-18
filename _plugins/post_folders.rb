# frozen_string_literal: true

# Folder posts: a note can live in its own folder in _posts/, with its files.
#
#   _posts/article1-rice-paddies/
#     2026-11-18-rice-paddies-from-space.md   <- the post (dated file name)
#     assets/anim_vh_season.mp4               <- its images, GIFs, videos,
#     assets/article1/fig_01.1.png               HTML figures, data files...
#
# 1. The other files of the folder are published next to the post's page, at the
#    same relative path, so `![...](assets/article1/fig_01.1.png)` works on the
#    site as it does in the VS Code Markdown preview. Markdown files are not
#    published (notes or a README can stay in the folder), nor are dotfiles and
#    anything matched by `exclude` in _config.yml.
# 2. In every post, a Markdown image that starts a paragraph (an image on its own
#    line, its caption on the next) gets the look of the theme's figure.liquid:
#    it fits the column, is centered, rounded and shadowed, zooms on click and
#    loads lazily. Images that already have a class are left alone, and so are
#    images inside a link (badges).
#
# One post per folder. Posts directly in _posts/ work as before.

module PostFolders
  FIGURE_CLASSES = "img-fluid rounded z-depth-1 d-block mx-auto mb-2"

  # A file of a post folder, written next to the post's page.
  class AssetFile < Jekyll::StaticFile
    def initialize(site, dir, name, url)
      super(site, site.source, dir, name)
      @url = url
    end

    attr_reader :url

    # Out of the sitemap, like everything under assets/ (see `defaults` in _config.yml).
    def data
      @data ||= super.merge("sitemap" => false)
    end
  end

  class Generator < Jekyll::Generator
    def generate(site)
      posts_dir = site.in_source_dir("_posts")
      markdown_exts = site.config["markdown_ext"].split(",").map { |ext| ".#{ext.strip.downcase}" }

      site.posts.docs.each do |post|
        folder = File.dirname(post.path)
        next unless folder.start_with?("#{posts_dir}/")

        folder_in_posts = folder.delete_prefix("#{posts_dir}/")
        # Relative links resolve against the page's folder: /blog/2026/name/
        page_dir = post.url.end_with?("/") ? post.url : File.dirname(post.url)

        # Same filtering as Jekyll's own reading of _posts/ (dotfiles, exclude, backups).
        site.reader.get_entries("_posts", folder_in_posts).each do |entry|
          next if markdown_exts.include?(File.extname(entry).downcase)

          source = File.join("_posts", folder_in_posts, entry)
          site.static_files << AssetFile.new(site, File.dirname(source), File.basename(source),
                                             File.join(page_dir, entry))
        end
      end
    end
  end

  # <p><img src="..." alt="..." />  ->  <p><img class="..." data-zoomable loading="lazy" src="..." alt="..." />
  FIGURE_IMG = %r{<p><img\b(?![^>]*\bclass=)}

  Jekyll::Hooks.register :posts, :post_convert do |post|
    attributes = %(class="#{FIGURE_CLASSES}" data-zoomable)
    attributes += ' loading="lazy"' if post.site.config["lazy_loading_images"]
    post.content = post.content.gsub(FIGURE_IMG, "<p><img #{attributes}")
  end
end
