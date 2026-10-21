"""Export a JSON content brief to a Markdown document."""
import argparse
import json
from pathlib import Path

REQUIRED = ('title', 'platform', 'audience', 'key_points', 'call_to_action')


def render_brief(data):
    if not isinstance(data, dict):
        raise ValueError('Content brief must be a JSON object.')
    for field in REQUIRED:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')
    for field in ('title', 'platform', 'audience', 'call_to_action'):
        if not isinstance(data[field], str) or not data[field].strip():
            raise ValueError(f'{field} must be a nonempty string.')
    points = data['key_points']
    if not isinstance(points, list) or not points or any(not isinstance(p, str) or not p.strip() for p in points):
        raise ValueError('key_points must be a nonempty list of nonempty strings.')
    lines = [f"# {data['title']}", '', f"**Platform:** {data['platform']}", f"**Audience:** {data['audience']}", '', '## Key Points', '']
    lines.extend(f'- {point}' for point in points)
    lines.extend(['', '## Call to Action', '', data['call_to_action'], ''])
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Export a JSON content brief to Markdown.')
    parser.add_argument('input', type=Path, help='Input JSON file')
    parser.add_argument('output', type=Path, help='Output Markdown file')
    args = parser.parse_args()
    try:
        with args.input.open(encoding='utf-8') as file:
            data = json.load(file)
        markdown = render_brief(data)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding='utf-8')
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(1, f'Error: {exc}\n')
    print(f'Exported: {args.output}')


if __name__ == '__main__':
    main()
