**MyBlog**

*Work in Progress*

A project using Django 1.10.

Dependencies:
Python 3.5+
Django 1.10+

Follows Best Practices

Two Scoops of Django
This project is in the process of being updated to follow best practices as outlined in Two Scoops of Django 1.8

Update Log:

6-JAN-2017 update:

    Added bootstrap
    Created a header to apply to all apps and placed it in the home directory's templates folder
    Created a home app that the index URL routes to.
    TODO - "About Me" and "contact" pages in the home app

    Filled out blog app so it's functional
    TODO - style detail view
    TODO - add unit tests to make sure my models are set up correctly and that I don't break them in the future


9-JAN-2017 update:

    Header:
        navbar
        logo
        favicon
        footer (maybe will get rid of this. not sure)
    Home:
        added jumbotron with JS parallax effet
        TODO - "about me" and "contact" pages
    Blog:
        made models manytomany so future views can link multiple categories per blog
        write tests for functions
    TODO - tests for views
    TODO - style detail view, decide how to organize links to categories and entries. Maybe drop down menus in header/jumbotron?

14-Jan-2017 update:

    Home:
        models and views complete for "about me" and "contact" pages
        TODO - style views. maybe combine with blog view in global CSS file
        TODO - write real bio
        TODO - implement form mixin for contact page

    Blog:
        re-wrote view so textfield in blog is marked as safe for HTML so I can add html tags to blog posts
        TODO - tests for views
        TODO - style detail view. maybe combined with About and Contact in global CSS file

    Style:
        started updating to match style guidelines in 2 Scoops of Django

    GIT:
        reorganized files in git-friendly way
        added .gitignore so I can push updates from the command line

    README:
        updated readme for style.
