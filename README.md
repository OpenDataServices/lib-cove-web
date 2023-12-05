# CoVE - Convert Validate & Explore

This repository contains code shared by standard-specific instances of the CoVE web app. Eg:

* Django stuff
* Commandline stuff
* HTML templates and CSS
* Helper functions

Currently it does *not* stand alone as a CoVE django app. 

## CoVEs which use this library

* [Beneficial Ownership Data Standard](https://github.com/openownership/cove-bods)
* [Open Contracting Data Standard](https://github.com/open-contracting/cove-ocds)
* [Open Contracting for Infrastructure Data Standards](https://github.com/open-contracting/cove-oc4ids)
* [IATI](https://github.com/opendataservices/cove)
* [360Giving](https://github.com/ThreeSixtyGiving/dataquality/)

## Theme customization

### Adding a link to the source control management (SCM) revision

We recommend [dealer](https://pypi.org/project/dealer/). To use it:

1. Add `dealer` to your requirements file
1. In your Django project's `settings.py` file:
    1. Set `DEALER_TYPE = 'git'`
    1. Add `'dealer.contrib.django.Middleware',` to the `MIDDLEWARE` list
1. In your Django app:
    1. Create a `templates/APP` directory, replacing `APP` with the name of your Django app
    1. Create a `base.html` file in the new directory, with at minimum:

        ```jinja
        {% extends 'base.html' %}
        {% load i18n %}
        ```

    1. Add to the `base.html` file, for example, replacing `OpenDataServices/cove` with the path to your GitHub repository:

        ```jinja
        {% block version_link %}
        <p class="text-muted">{% blocktrans %}Running version {% endblocktrans %}<a href="https://github.com/OpenDataServices/cove/tree/{{ request.tag }}">{{ request.tag }}</a></p>
        {% endblock %}
        ```

## Translations

We use Django's translation framework to provide this application in different languages.
We have used Google Translate to perform initial translations from English, but expect those translations to be worked on by humans over time.

### Translations for Translators

Translators can provide translations for this application by becomming a collaborator on Transifex https://www.transifex.com/OpenDataServices/cove

### Translations for Developers

For more information about Django's translation framework, see https://docs.djangoproject.com/en/1.8/topics/i18n/translation/

#### Adding new text

In short:

* Add strings in a way that makes them translatable.
* Extract the messages and push them to transifex.
* When translations are ready, pull them from transifex.
* Bump the minor version number.
* Update dependent CoVEs (see list above) to use the new version, so they get the new strings. 

If you add new text to the interface, ensure to wrap it in the relevant gettext blocks/functions.

In order to generate messages and post them on Transifex:

First check the `Transifex lock <https://opendataservices.plan.io/projects/co-op/wiki/CoVE_Transifex_lock>`, because only one branch can be translated on Transifex at a time.

Then:

    python manage.py makemessages -l en
    tx push -s

In order to fetch messages from transifex:

    tx pull -a

In order to compile them:

    python manage.py compilemessages

Keep the makemessages and pull messages steps in thier own commits seperate from the text changes.

To check that all new text is written so that it is able to be translated you could install and run `django-template-i18n-lint`

    pip install django-template-i18n-lint
    django-template-i18n-lint cove

## Command Line Interface

TODO
