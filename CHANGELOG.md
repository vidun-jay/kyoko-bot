# Changelog
All notable changes to this project will be documented in this file.

## [1.0.8] - 2022-10-23
### Changed
- Fixed the description thing - reacting to the message now shows the corresponding description

## [1.0.7] - 2022-10-22
### Added
- Displays description upon reaction (granted not the right one, but hey it's something)
- `get_url()` function
- `get_description` function

## [1.0.6] - 2022-10-10
### Changed
- Bug displayed results starting from the second result instead of top result
- Needed to make some variables global, working on a way around this

## [1.0.5] - 2022-10-10
### Changed
- `animeSearch` is now it's own function to make code a bit more modular

## [1.0.4] - 2022-10-09
### Added
- Numbering for results
- Reactions

### Changed
- Returns top 5 results instead of 10

### Removed
- `sentenceCase()` function (useless)

## [1.0.3] - 2022-10-09
### Changed
- `!anime` command returns basic HTML parsing, instead of just URL


## [1.0.2] - 2022-10-08
### Changed
- Uses embed instead of message

### Added
- `SentenceCase()` method

## [1.0.1] - 2022-10-08
### Changed
- `!anime` searches specifically for anime instead of all mediums
- Added docstrings for functions
- If condition uses channel variable

### Added
- `CHANGELOG.md`

## [1.0.0] - 2022-10-08
### Added
- Initial release