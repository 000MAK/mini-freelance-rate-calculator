# Mini Freelance Rate Calculator

Estimates direct-cost-adjusted hourly earnings and compares them with a configurable hourly floor.

## Requirements

- Python 3.10+
- Standard library only; no `pip install` step required.

## Run

```bash
python main.py --help
```

## Example

`python main.py --price 75 --fee 7.5 --cost 2 --reserve 5 --minutes 90`

## Tests

```bash
python -m unittest discover -s tests -v
```

## Safety notes

Use copies of important files. Review output before using it in production. Do not add credentials, private data, or real customer files to Git.

## License

MIT. See [LICENSE](LICENSE).
