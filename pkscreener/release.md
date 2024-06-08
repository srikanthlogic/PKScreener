[![MADE-IN-INDIA](https://img.shields.io/badge/MADE%20WITH%20%E2%9D%A4%20IN-INDIA-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/India) [![GitHub release (latest by date)](https://img.shields.io/github/v/release/pkjmesra/PKScreener?style=for-the-badge)](#) [![GitHub all releases](https://img.shields.io/github/downloads/pkjmesra/PKScreener/total?color=Green&label=Downloads&style=for-the-badge)](#) [![MADE_WITH](https://img.shields.io/badge/BUILT%20USING-PYTHON-yellow?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)

## What's New?
1. [v0.45.20240607.444] release
* Sound alerts for configured options in pkscreener.ini when running in monitoring mode (option -m)
* Moved the telegram image quality/size and compression parameters to pkscreener.ini to make it configurable and under control.
* Defined configurable option for sleep interval between data fetches for pinned scanners. Check out pinnedmonitorsleepintervalseconds value in pkscreener.ini config file.
* Defined configurable market-open and close hour:minute in pkscreener.ini config file so that if you would like pre-open-market-data as well, you can configure it and run it locally.
* Fixed a bug for piped scanners wherein after being pinned, it was not updating the data regularly.
* Docker builds for multi-arch fixed. Now you have docker build targeted at amd64, arm/v7 as well as arm64 architectures. Download docker desktop now and run with "docker run -it pkjmesra/pkscreener:latest" Enjoy!
* Added a Quick Backtest Mode (Try T > B followed by the n-th day/candle) for which you'd like to get the maximum potential profitability analysis.
* Added many new pre-defined piped scanner
* Modified ATR trailing stop scanner to get better results. Try X > 12 > 30.
* Telegram bot reverted back to the older non-LGPL licensed version
* Moved a number of columns to always-hidden-columns in the pkscreener.ini config file. You can edit it to show the hidden columns on your console.
* Now set how many results you want displayed by changing the number maxdisplayresults in pkscreener.ini
* Run scans over the index, by choosing index option 0 and providing the index symbol like ^NSEI etc. You should know the index symbol on your own(Yahoo finance?) and it must start with ^
* You can now pin the just-finished-scan even when the result count is zero.
* NOTE: To fit all result columns on your screen, switch to smaller font size in your console.

## Older Releases
* [https://github.com/pkjmesra/PKScreener/releases] : Discarded to save on storage costs!

## Downloads
| Operating System                                                                                         | Executable File                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) | **[pkscreenercli.exe](https://github.com/pkjmesra/PKScreener/releases/download/0.45.20240607.444/pkscreenercli.exe)**                                                                                                         |
| ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)       | **[pkscreenercli.bin](https://github.com/pkjmesra/PKScreener/releases/download/0.45.20240607.444/pkscreenercli.bin)**                                                                                                         |
| ![Mac OS](https://img.shields.io/badge/mac%20os-D3D3D3?style=for-the-badge&logo=apple&logoColor=000000)  | **[pkscreenercli.run](https://github.com/pkjmesra/PKScreener/releases/download/0.45.20240607.444/pkscreenercli.run)** ([Read Installation Guide](https://github.com/pkjmesra/PKScreener/blob/main/INSTALLATION.md#for-macos)) |

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
