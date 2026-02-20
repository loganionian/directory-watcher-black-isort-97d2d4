# directory-watcher-black-isort

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A CLI tool that watches a directory for changes and auto-formats Python files on save using Black and isort, with git-hook integration.

## The Problem

Manually formatting code can be time-consuming and lead to inconsistencies. This tool automates formatting on file save, ensuring adherence to style guides.

## How It Works

The tool would use `watchdog` to monitor file changes and trigger Black and isort for formatting. Git hooks would allow for smooth integration into the development workflow.

## Features

- Configurable watch directories and file types.
- Options to enable/disable formatting on save.
- Integration with various editors like VSCode and PyCharm.
- Logging of formatting actions for easier debugging.

## Installation

```bash
pip install directory-watcher-black-isort
```

Or install from source:

```bash
git clone https://github.com/YOUR_USERNAME/directory-watcher-black-isort.git
cd directory-watcher-black-isort
pip install -e .
```

## Quick Start

```python
# Example configuration for the directory watcher
{
    "watch_directory": "src/",
    "format_on_save": true,
    "black_args": ["--fast"],
    "isort_args": ["--profile", "black"]
}
```

## Tech Stack

- Primary library/framework: `watchdog` for monitoring file changes.
- Supporting library: `black` and `isort` for automatic code formatting.

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.
