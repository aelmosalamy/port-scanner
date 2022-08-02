# Port Scanner

Basic port scanner written in Python.

## Usage

Basic usage:
```shell
# Perform a TCP scan against `localhost` ports 20 to 25, 80 and 443
python main.py -p 20-25,80,443 localhost
```

You can always see what arguments are available to you using:
```shell
python main.py -h
```

## Roadmap

- [x] CLI interface
- [x] Flexible port parser
- [x] TCP connect scan
- [ ] TCP half-handshake scan (stealth scan)
- [ ] TCP NULL, FIN scans
- [ ] UDP scan
- [ ] Output results in a parsable format
- [ ] Refactor, split scanning/logging

## Motivation

I intend with this project to create a:
- Functional port scanner.
- Well-commented, friendly codebase to help InfoSec students learn how their tools work.

## Contribution

This project uses Python3 and requires the following external dependencies:
- `plac` (Easy to use arguments parser)