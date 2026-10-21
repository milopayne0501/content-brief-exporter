# Content Brief Exporter CLI

Convert structured JSON content briefs into readable Markdown documents. Designed as a reusable utility for an AI content automation workflow.

## Features
- JSON input and Markdown output
- Required-field and type validation
- Helpful errors for invalid or missing files
- No third-party dependencies

## Technologies
Python 3.9+ (standard library only)

## Run
```bash
python export_brief.py sample_brief.json output.md
```

## Test
```bash
python -m unittest discover -v
```

## Example
Input: `sample_brief.json`. Output: `output.md`, with a title, platform, audience, bullet-point key points, and a call to action.

## What I learned
How to validate JSON content, format Markdown strings, export files, and test both normal and invalid input.

## Future improvements
Support optional brief sections or integration into AI Content Automation after the standalone tool is complete.
