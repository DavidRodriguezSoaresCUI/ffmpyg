# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

<!-- As much as possible use subsections: Added, Removed, Modified, BugFix -->

## [0.0.3] - 23.04.2023

### Added

- Modules `ffmpeg_vmaf` and `virtualfs`

### Modified

- `ffmpeg_command.build_ffmpeg_command`: Arguments are now aligned with doc on optional typing
- Moved `assert_ffmpeg_supports_vmaf` from `ffmpeg_lib` to `ffmpeg_vmaf`

### Removed

- Vestigial `main` code in some modules

## [0.0.2] - 23.04.2023

### Added

- `ffmpeg_lib`: created with 3 methods
- `.gitignore`: Exclusions for generated doc
- Added forgotten initial release entry

## BugFix

- `analyze_code.bat`: reduced scope to files in ``src``

## [0.0.1] - 22.04.2023

__INITIAL RELEASE__