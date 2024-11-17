#!/usr/bin/env python3
import toml
import sys


def pyproject_check(file_path="pyproject.toml"):
    try:
        with open(file_path, "r") as file:
            pyproject = toml.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        sys.exit(1)
    except toml.TomlDecodeError:
        print(f"Error: {file_path} contains invalid TOML.")
        sys.exit(1)

    uv_sources = pyproject.get('tool', {}).get('uv', {}).get('sources', {})

    error_count = 0
    for key, source in uv_sources.items():
        if isinstance(source, dict) and 'path' in source:
            print(f"Local path found in [tool.uv.sources]: {key} -> {source['path']}")
            error_count += 1

    if error_count:
        sys.exit(1)

    print("No local paths found in [tool.uv.sources].")
    sys.exit(0)

def main():
    pyproject_check()

if __name__ == "__main__":
    pyproject_check()
