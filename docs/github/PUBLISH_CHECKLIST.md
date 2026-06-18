# GitHub Publish Checklist

Before publishing:

- [ ] Run `python t_cli.py demo`
- [ ] Run `python t_cli.py backtest`
- [ ] Run `pytest -q`
- [ ] Run Docker build
- [ ] Confirm `.env` is not committed
- [ ] Confirm no API keys
- [ ] Confirm README quickstart works
- [ ] Confirm LICENSE, DISCLAIMER, SECURITY exist
- [ ] Tag as `v0.8.0-alpha`
- [ ] Add screenshots/video if available
