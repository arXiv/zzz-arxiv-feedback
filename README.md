# arxiv-feedback

Feedback collection, bug reports, as a pluggable Flask blueprint.

## Objectives

This project provides a pluggable Flask blueprint that provides the following
functionality for arXiv apps.

### In v0.1:

1. Provide a splash page that describes how users can help to improve the
   application.

   - For bug reports/feature requests, links out to issue tracker of
     corresponding repository.
   - For developers, links out to guide for contributors of corresponding
     repository.

2. Provide a standardized "Help Improve This" button macro that can placed on
   any arXiv page, that links to the splash page.


### In v0.2:

3. Provide a Lichert-style feedback widget, and a backing API, that allows
   users to provide rapid feedback on new features.
