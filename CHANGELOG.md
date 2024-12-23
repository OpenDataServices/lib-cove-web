# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.31.1] - 2024-10-23

## Fixed

- Fixed string formatting for the "The request timed out after %(timeout)s seconds" error

## [0.31.0] - 2024-10-16

Note: Release 0.30.5 was not done properly and was missing some code.

### Added

- Add `lang` attribute to `html` tag.

### Fixed

- If a file is expired, the error message states the correct DELETE_FILES_AFTER_DAYS value, instead of the default of 7.
- If a file is expired, the "file not found" exception is caught by all possible sources.

## [0.30.5] - 2024-09-30

### Added

- New setting `allow_direct_web_fetch` to configure whether cove will fetch any url passed as a GET parameter rather than from the input form. The default will be for this to be disabled. Cove implementations updating may need to check if there are "try this sample data" links on the home page that will need to be updated to use a form with newly required CSRF protection (For example - https://github.com/OpenDataServices/lib-cove-web/pull/144#issuecomment-2378743354).
- Set the `REQUESTS_TIMEOUT` setting, to prevent source URLs from causing a denial of service, whether accidentally or maliciously.

## [0.30.4] - 2024-06-28

### Fixed

- Report a human-readable error when an invalid URL for the input data is supplied by the user. https://github.com/OpenDataServices/lib-cove-web/pull/139

## [0.30.3] - 2024-05-29

### Fixed

- Unsuccessful implmentation of human-readable error, see 0.30.4 above.

## [0.30.2] - 2024-01-30

### Fixed

- support_email was in templates but was not set anywhere. Set in views and set in config.
  https://github.com/OpenDataServices/lib-cove-web/issues/101

## [0.30.1] - 2023-12-05

### Fixed

- Spacing in a Spanish translation https://github.com/OpenDataServices/lib-cove-web/pull/129

## [0.30.0] - 2023-12-01

### Removed / Changed

- Link to http://datapipes.herokuapp.com in cove/templates/additional_codelist_values.html - instead link direct to URL.
  https://github.com/OpenDataServices/lib-cove-web/issues/74
  The datapipes app was shutdown in Aug 2022, so this feature has been showing users links that 404 for a while.
  So while this removal may seem like a breaking change, it actually makes things better for users.
  See issue for discussion about fixes.

## [0.29.0] - 2023-11-09

### Removed

- Dropped support for Python 3.7, as it is now end of life.
- Remove django-environ dependency https://github.com/OpenDataServices/lib-cove-web/issues/80
  If you use this dependency directly, add it to your requirements file.

### Fixed

- Fix the "null" key in validation_error_template_lookup_safe
  https://github.com/OpenDataServices/lib-cove-web/pull/122
  https://github.com/OpenDataServices/lib-cove-web/pull/123 

## [0.28.0] - 2023-07-13

### Add

- Support Django 4.2 https://github.com/OpenDataServices/lib-cove-web/issues/112

### Fixed

- Add missing, or remove extra, spaces around HTML tags, named placeholders and punctuation in Spanish translations
- Add database migration for 0.27.0 changes

## [0.27.0] - 2023-03-06

## Changed

- Randomize the uploaded file subdirectory, to allow coves to hide original files from unauthenticated users

## [0.26.0] - 2023-02-17

## Changed

- Switch to Werkzeug from uc-rfc6266-parser
- Drop Python 3.6 support
- Use FieldFile.path instead of File.name, to avoid unclosed file warnings

## [0.25.0] - 2022-07-19

### Add

- Store the original form parameters that were used when submitting the data. Allowing for users of lib-cove-web to create custom actions based on the input.

### Removed

- "Tool is Alpha" content from banner block in base template


## [0.24.2] - 2021-11-18

- Do not warn if `SECRET_KEY` is not set in settings

## [0.24.1] - 2021-05-25

### Fixed

- Include .mo files in the PyPI package

## [0.24.0] - 2021-05-25

### Changed

- Add support to `html_error_msg` for messages about a non-unique combination of multiple IDs. (E.g. ocid and id, as added in [this lib-cove-ocds PR](https://github.com/open-contracting/lib-cove-ocds/pull/91)).
- `.mo` files are commited now, so we don't have to rely on the parent cove project finding them with `compilemessages` https://github.com/open-contracting/deploy/issues/269

## [0.23.0] - 2021-05-12

### Removed

- Remove [Dealer](https://github.com/OpenDataServices/lib-cove-web/pull/90) (git commit info), [Django Debug Toolbar](https://github.com/OpenDataServices/lib-cove-web/pull/88/files) and [Sentry](https://github.com/OpenDataServices/lib-cove-web/pull/92) integration, so that projects can choose whether to use them or not. Projects will **need to explicitly add these** themselves to keep the same functionality.
- Empty dataload app has been removed https://github.com/OpenDataServices/lib-cove-web/pull/87/files

### Changed

- Make sure requirements are correct https://github.com/OpenDataServices/lib-cove-web/pull/85
- `PIWIK` and `GOOGLE_ANALYSTICS_ID` are now optional in the settings https://github.com/OpenDataServices/lib-cove-web/pull/94
- Don't show section on Sentry in the terms and conditions, if its not in use https://github.com/OpenDataServices/lib-cove-web/pull/95

## [0.22.0] - 2021-04-14

### Added

- Add Django 3.x support https://github.com/OpenDataServices/lib-cove-web/pull/79

## [0.21.1] - 2021-04-08

### Fixed

- Switch to a fork of the rfc6266 package, that supports Python 3.8

## [0.21.0] - 2021-03-25

### Changed

- All text that might appear in cove-ocds is translated into Spanish https://github.com/open-contracting/cove-ocds/issues/144

### Fixed

- Codelist csv link now points to working service. https://github.com/OpenDataServices/lib-cove-web/issues/74

## [0.20.0] - 2021-02-10

### Added

- Number of days before files expire is now configurable in settings.py https://github.com/open-contracting/cove-ocds/issues/142

## [0.19.0] - 2021-01-26

### Changed

- Make `html_error_msg` importable from its own file, and without Django settings needing to be configured (e.g. in lib-cove-bods).

## [0.18.4] - 2020-12-18

### Fixed

- Fix 'NoneType' object has no attribute 'format', due to validation error messages we don't override

## [0.18.3] - 2020-12-16

### Fixed

- Make tables fixed layout to avoid layout breaking on long unbroken text
- Fix `NameError` due to `e_instance` not being defined

## [0.18.2] - 2020-11-05

### Fixed

- Add a missing string to the translation https://github.com/OpenDataServices/lib-cove-web/pull/60

## [0.18.1] - 2020-10-22

### Fixed

- Don't require `VALIDATION_ERROR_LOCATIONS_LENGTH` and `VALIDATION_ERROR_LOCATIONS_SAMPLE` to be in the settings file
- Fixes for translation work in 0.18.0 to work with [360Giving and IATI CoVEs](https://github.com/OpenDataServices/cove/)

## [0.18.0] - 2020-10-19

### Changed

See https://github.com/OpenDataServices/lib-cove-web/pull/58 for the below:

- Move strings from lib-cove to here, so they're easier to translate
- Copy a strings for minProperties here from jsonschema, so it can be translated
- Add Spanish translation for all strings

## [0.17.0] - 2020-09-16

### Add

- Make it possible to set a limit on the number of locations shown for an error, and optionally randomise them if there are too many.

### Changed

- Add 'Co-operative' to 'built by'.

## [0.16.0] - 2020-08-27

### Fixed

- The package available in PyPi was not including all files correctly.

### Changed

- Move requirements into setup.py and delete requirements.\* files

## [0.15.0] - 2020-08-20

### Add

- Add xml content types to auto detection https://github.com/OpenDataServices/cove/issues/1283

### Changed

- Break up some terms templates to allow OCDS specific overrides
- Delete OCDS and 360 logos. They are saved in cove/cove-ocds and cove-opendataservices-coop repositories.
- Delete lib-cove-web/cove/templates/multi_index.html. Not being used (it was replaced by the static site at 
cove-opendataservices-coop).

## [0.14.0] - 2020-04-28

### Changed

- Changes needed to update 360/IATI cove to Django 2.2 LTS
- Switch to sentry-sdk from raven

## [0.13.0] - 2020-04-23

### Changed

- Update Django to 2.2 LTS

## [0.12.0] - 2020-03-11

### Add

- Text added to show awareness of Open Document Support that is now available in flatten-tool 0.11.0 and current CoVE.

## [0.11.0] - 2020-02-17

### Changed

- Split terms.html into many templates using includes
(This make it possible for instances of COVE to add extra trackers)
- Add Terms for Google Analytics, behind a config switch
(The actual tracking code for Google Analytics is in this library (behind a config switch) so the terms and conditions should be too.)

## [0.10.0] - 2019-11-27

### Changed

- Input template is rendered via `COVE_CONFIG` so individual CoVEs can override it.

## [0.9.2] - 2019-07-04

- Update 360Giving's address

### Changed

- 360Giving's address updated in Ts&Cs

## [0.9.1] - 2019-06-18

### Changed

- Update lib-cove requirment to 0.7.0

## [0.9.0] - 2019-06-10

### Added

- Add template displaying all additional fields.

## [0.8.0] - 2019-04-25

### Added

- Add filter list_from_attribute.

## [0.7.0] - 2019-04-02

### Added

- Add a block for about links, so that BODS CoVE can overwrite https://github.com/openownership/cove-bods/issues/25

## [0.6.0] - 2019-03-28

### Added

- Fields `file_name` and `created_time` in explore_data_context.

## [0.5.0] - 2019-03-22

### Added

- Allow the version link to be overrided in the template

## [0.4.0] - 2019-03-14

### Added

- Pass the original file path into the context

### Fixed

- Fix typo in the following text: "all data **suplied** to this website is automatically deleted"


## [0.3.0] - 2019-01-07

### Added

- Display an error's line number if available (currently only IATI)

## [0.2.0] - 2018-12-05

### Changed

- Update Transifex config: changed resource name to `cove-common`
- Add English message files and Spanish translations

## [0.1.0] - 2018-11-28

- First Release
