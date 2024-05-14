[![MADE-IN-INDIA](https://img.shields.io/badge/MADE%20WITH%20%E2%9D%A4%20IN-INDIA-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/India) [![GitHub release (latest by date)](https://img.shields.io/github/v/release/pkjmesra/PKScreener?style=for-the-badge)](#) [![GitHub all releases](https://img.shields.io/github/downloads/pkjmesra/PKScreener/total?color=Green&label=Downloads&style=for-the-badge)](#) [![MADE_WITH](https://img.shields.io/badge/BUILT%20USING-PYTHON-yellow?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)

## What's New?
1. [v0.44.20240514.371] release
* High Momentum scanner added. Try X > 12 > 31.
* Now, change config periods using menus within the app (1d, 280d, 1m, 5m, 30m, 1H, 1d, 1w, 1M)
* ATR Trailing Stops scanner for Swing Paper Trading analysis added. Try out X > 12 > 30 > (1 for Buy, 2 for Sell). You can change the sensitivity and atr periods in the config file.
* Bid/Ask build up scanner added. Try X > 12 > 29. Best to use this as a piped scanner to avoid getting blocked or rate-limited from NSE. For example, use -o "X:12:9:2.5:;|X:0:29" instead of X:12:29. This piped result can also be enabled in the telegram bot now during trade hours under Intraday Monitor.
* Added ability to filter your results. For now you can filter using the defined keys in the filters section of user config file. For example, to only show those stocks that have changed by at least 4% and have volume more than 9 million, you can change the config to:

  minimumchangepercentage = 4
  minimumvolume = 9000000

* New scanner: 'ATR cross' added. Try X > 12 > 27 . It's now sorted by descending ATR instead of volume.
* New scanner: 'Bullish Higher Opens' added. Try X > 12 > 28
* Performance improvements to have the scans finish within 40 seconds for most cases on Mac/Ubuntu and within 60 seconds on Windows.
* Monitoring dashboard added (with option --monitor "X") or just use the menu 'Monitor Intraday'. See --help option to see all command options. Configure how many and what scanners you want in the config file.
* Intraday monitoring now available as part of telegram bot @nse_pkscreener_bot
* MacOS failing builds fixed.
* Menus had disappeared on Windows. That's fixed now. You should see all menus.
* Export to Excel is working back again! It was broken inadvertently for a while. Thanks for reporting!
* Monitoring, download data as pkl (both daily and intraday), and enabling logging from within the console app via menus is now added.
* Piping the results from previous scans to the next one is added for all standard screener options (for example X:12:9:2.5;|X:12:23 will first scan all volume gaimers and then only scan for ATR cross from within those volume gainers). Use ; and | to separate scans and pipe results. Piping for monitoring dashboard is enabled as well but using , instead of ;.
* Multiple other bug fixes.
* NOTE: To fit all result columns on your screen, switch to smaller font size in your console.

## Older Releases
* [https://github.com/pkjmesra/PKScreener/releases] : Discarded to save on storage costs!

## Downloads
| Operating System                                                                                         | Executable File                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) | **[pkscreenercli.exe](https://github.com/pkjmesra/PKScreener/releases/download/0.44.20240503.326/pkscreenercli.exe)**                                                                                                         |
| ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)       | **[pkscreenercli.bin](https://github.com/pkjmesra/PKScreener/releases/download/0.44.20240503.326/pkscreenercli.bin)**                                                                                                         |
| ![Mac OS](https://img.shields.io/badge/mac%20os-D3D3D3?style=for-the-badge&logo=apple&logoColor=000000)  | **[pkscreenercli.run](https://github.com/pkjmesra/PKScreener/releases/download/0.44.20240503.326/pkscreenercli.run)** ([Read Installation Guide](https://github.com/pkjmesra/PKScreener/blob/main/INSTALLATION.md#for-macos)) |

## How to use?

[**Click Here**](https://github.com/pkjmesra/PKScreener) to read the documentation. You can also read it at https://pkscreener.readthedocs.io/en/latest/?badge=latest

## Join our Community Discussion

[**Click Here**](https://github.com/pkjmesra/PKScreener/discussions) to join the community discussion and see what other users are doing!

## Facing an Issue? Found a Bug?

[**Click Here**](https://github.com/pkjmesra/PKScreener/issues/new/choose) to open an Issue so we can fix it for you!

## Want to Contribute?

[**Click Here**](https://github.com/pkjmesra/PKScreener/blob/main/CONTRIBUTING.md) before you start working with us on new features!

## Disclaimer:
* DO NOT use the result provided by the software solely to make your trading decisions.
* Always backtest and analyze the stocks manually before you trade.
* The Author(s) and the software will not be held liable for any losses.

## License
* MIT: https://github.com/pkjmesra/PKScreener/blob/main/LICENSE
