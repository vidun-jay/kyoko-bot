# Changelog
All notable changes to this project will be documented in this file.

## [1.2.0] 2023-07-18
### Added
- Added `!manga` command  

## [1.1.1] 2022-12-28
### Added
- `!profile` command
- Returns anime stats properly, still need to add manga stats

### Changed
- Created separate `AnimeSearch.py` and `ProfileSearch.py` files for their respective functions to clean up `main` a little bit

## [1.1.0] 2022-12-26
### Added
- Anime search now also shows image

## [1.0.9] 2022-12-26
### Changed
- Fixed off-by-one search error on line 70
- Made docstrings more readable

### Added
- New selection edits message instead of sending new one
- Reacting to message now unreacts immediately (for aesthetics)

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