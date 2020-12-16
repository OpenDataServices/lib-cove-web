# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
