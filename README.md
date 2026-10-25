# Mini Freelance Rate Calculator

A small Python command-line utility that estimates net task revenue after specified direct costs and calculates the corresponding hourly rate.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## What it calculates

- Estimated net amount: quoted price minus platform fee, direct task costs, and a revision reserve.
- Estimated hourly return: estimated net amount divided by the estimated work duration.
- A simple comparison against a configurable hourly-rate floor.

The calculator labels the result `CONSIDER` when the estimated rate meets the chosen floor and `BELOW_FLOOR` otherwise.

## Requirements

- Python 3.10 or later
- No third-party package installation required

## Quick start

Show command options:

```bash
python main.py --help
```

Example: estimate net and hourly return for a $75 task with $7.50 in fees, $2 in direct costs, a $5 revision reserve, and 90 minutes of work:

```bash
python main.py --price 75 --fee 7.5 --cost 2 --reserve 5 --minutes 90
```

Set a different target floor with `--floor`. The default is $30/hour.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Interpretation and limitations

This is a planning aid, not a guarantee of income or a quote recommendation. The estimate does not automatically include taxes, fixed overhead, unpaid time, payment delays, foreign-exchange conversion, or all platform-specific charges. Include relevant costs yourself and use realistic time estimates.

## Related Quantix projects

- [Quantix 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)
- [Mini CSV Cleaner](https://github.com/000MAK/mini-csv-cleaner)
- [All public repositories](https://github.com/000MAK?tab=repositories)

## Safety

Do not include private client details or actual financial account data in public examples.

## License

MIT. See [LICENSE](LICENSE).
