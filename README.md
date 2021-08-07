# Bouman Group Website

## Acknowledgments
Most code is based off of [Peter Anderson's website](https://github.com/peteanderson80/peteanderson80.github.io),
which is a fork of [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes).

## Commands
### Serve at localhost:4000
```
$ bundle exec jekyll build
$ bundle exec jekyll serve
```

### Rebuild css from _scss
```
$ npm run build:css
```

## Editing Content
* News: `_data/news.yml`
* People: `_data/people.yml`
* Publications: `_data/publications.yml`
* Highlighted Projects section: `_data/publications.yml` (under "highlight")
* About section: `_includes/about.md`

**Note**: Most fields will Markdown-ified.

### TODOs
* Indicate current page in navbar.