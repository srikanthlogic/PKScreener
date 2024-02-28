"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""

from PKDevTools.classes.ColorText import colorText

from pkscreener.classes.Pktalib import pktalib
from PKDevTools.classes.log import measure_time

class CandlePatterns:
    reversalPatternsBullish = [
        "Morning Star",
        "Morning Doji Star",
        "3 Inside Up",
        "Hammer",
        "3 White Soldiers",
        "Bullish Engulfing",
        "Dragonfly Doji",
        "Supply Drought",
        "Demand Rise",
    ]
    reversalPatternsBearish = [
        "Evening Star",
        "Evening Doji Star",
        "3 Inside Down",
        "Inverted Hammer",
        "Hanging Man",
        "3 Black Crows",
        "Bearish Engulfing",
        "Shooting Star",
        "Gravestone Doji",
    ]

    def __init__(self):
        pass

    @measure_time
    # Find candle-stick patterns
    # Arrange if statements with max priority from top to bottom
    def findPattern(self, data, dict, saveDict):
        data = data.head(4)
        data = data[::-1]
        existingPattern = ''
        if "Pattern" in saveDict.keys():
            existingPattern=f'{(", "+saveDict["Pattern"]) if saveDict["Pattern"] is not None else ""}'
            if existingPattern == ", ":
                existingPattern = ""
        else:
            saveDict["Pattern"] = ""
            dict["Pattern"] = ""
        # Only 'doji' and 'inside' is internally implemented by pandas_ta.
        # Otherwise, for the rest of the candle patterns, they also need
        # TA-Lib.
        check = pktalib.CDLDOJI(data["Open"], data["High"], data["Low"], data["Close"])
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = colorText.BOLD + f"Doji{existingPattern}" + colorText.END
            saveDict["Pattern"] = f"Doji{existingPattern}"
            return True

        check = pktalib.CDLMORNINGSTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.GREEN + f"Morning Star{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Morning Star{existingPattern}"
            return True

        check = pktalib.CDLMORNINGDOJISTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.GREEN + f"Morning Doji Star{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Morning Doji Star{existingPattern}"
            return True

        check = pktalib.CDLEVENINGSTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.FAIL + f"Evening Star{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Evening Star{existingPattern}"
            return True

        check = pktalib.CDLEVENINGDOJISTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.FAIL + f"Evening Doji Star{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Evening Doji Star{existingPattern}"
            return True

        check = pktalib.CDLLADDERBOTTOM(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.GREEN + f"Bullish Ladder Bottom{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"Bullish Ladder Bottom{existingPattern}"
            else:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.FAIL + f"Bearish Ladder Bottom{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"Bearish Ladder Bottom{existingPattern}"
            return True

        check = pktalib.CDL3LINESTRIKE(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.GREEN + f"3 Line Strike{existingPattern}" + colorText.END
                )
            else:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.FAIL + f"3 Line Strike{existingPattern}" + colorText.END
                )
            saveDict["Pattern"] = f"3 Line Strike{existingPattern}"
            return True

        check = pktalib.CDL3BLACKCROWS(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.FAIL + f"3 Black Crows{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"3 Black Crows{existingPattern}"
            return True

        check = pktalib.CDL3INSIDE(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.GREEN + f"3 Inside Up{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"3 Outside Up{existingPattern}"
            else:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.FAIL + f"3 Inside Down{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"3 Inside Down{existingPattern}"
            return True

        check = pktalib.CDL3OUTSIDE(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.GREEN + f"3 Outside Up{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"3 Outside Up{existingPattern}"
            else:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.FAIL + f"3 Outside Down{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"3 Outside Down{existingPattern}"
            return True

        check = pktalib.CDL3WHITESOLDIERS(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.GREEN + f"3 White Soldiers{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"3 White Soldiers{existingPattern}"
            return True

        check = pktalib.CDLHARAMI(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.GREEN + f"Bullish Harami{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"Bullish Harami{existingPattern}"
            else:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.FAIL + f"Bearish Harami{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"Bearish Harami{existingPattern}"
            return True

        check = pktalib.CDLHARAMICROSS(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (
                    colorText.BOLD
                    + colorText.GREEN
                    + f"Bullish Harami Cross{existingPattern}"
                    + colorText.END
                )
                saveDict["Pattern"] = f"Bullish Harami Cross{existingPattern}"
            else:
                dict["Pattern"] = (
                    colorText.BOLD
                    + colorText.FAIL
                    + f"Bearish Harami Cross{existingPattern}"
                    + colorText.END
                )
                saveDict["Pattern"] = f"Bearish Harami Cross{existingPattern}"
            return True

        check = pktalib.CDLMARUBOZU(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (
                    colorText.BOLD
                    + colorText.GREEN
                    + f"Bullish Marubozu{existingPattern}"
                    + colorText.END
                )
                saveDict["Pattern"] = f"Bullish Marubozu{existingPattern}"
            else:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.FAIL + f"Bearish Marubozu{existingPattern}" + colorText.END
                )
                saveDict["Pattern"] = f"Bearish Marubozu{existingPattern}"
            return True

        check = pktalib.CDLHANGINGMAN(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.FAIL + f"Hanging Man{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Hanging Man{existingPattern}"
            return True

        check = pktalib.CDLHAMMER(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.GREEN + f"Hammer{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Hammer{existingPattern}"
            return True

        check = pktalib.CDLINVERTEDHAMMER(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.GREEN + f"Inverted Hammer{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Inverted Hammer{existingPattern}"
            return True

        check = pktalib.CDLSHOOTINGSTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.FAIL + f"Shooting Star{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Shooting Star{existingPattern}"
            return True

        check = pktalib.CDLDRAGONFLYDOJI(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.GREEN + f"Dragonfly Doji{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Dragonfly Doji{existingPattern}"
            return True

        check = pktalib.CDLGRAVESTONEDOJI(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (
                colorText.BOLD + colorText.FAIL + f"Gravestone Doji{existingPattern}" + colorText.END
            )
            saveDict["Pattern"] = f"Gravestone Doji{existingPattern}"
            return True

        check = pktalib.CDLENGULFING(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (
                    colorText.BOLD
                    + colorText.GREEN
                    + f"Bullish Engulfing{existingPattern}"
                    + colorText.END
                )
                saveDict["Pattern"] = f"Bullish Engulfing{existingPattern}"
            else:
                dict["Pattern"] = (
                    colorText.BOLD
                    + colorText.FAIL
                    + f"Bearish Engulfing{existingPattern}"
                    + colorText.END
                )
                saveDict["Pattern"] = f"Bearish Engulfing{existingPattern}"
            return True

        return False
