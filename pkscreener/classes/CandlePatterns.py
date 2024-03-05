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
# from PKDevTools.classes.log import measure_time

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

    def findCurrentSavedValue(self, screenDict, saveDict, key):
        existingScreen = screenDict.get(key)
        existingSave = saveDict.get(key)
        existingScreen = f"{existingScreen}, " if (existingScreen is not None and len(existingScreen) > 0) else ""
        existingSave = f"{existingSave}, " if (existingSave is not None and len(existingSave) > 0) else ""
        return existingScreen, existingSave

    #@measure_time
    # Find candle-stick patterns
    # Arrange if statements with max priority from top to bottom
    def findPattern(self, data, dict, saveDict):
        data = data.head(4)
        data = data[::-1]
        existingPattern = ''
        hasCandleStickPattern = False
        if "Pattern" in saveDict.keys():
            existingPattern=f'{(", "+dict["Pattern"]) if saveDict["Pattern"] is not None else ""}'
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
            dict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + colorText.BOLD + f"Doji" + colorText.END + existingPattern
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Doji{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLMORNINGSTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.GREEN + f"Morning Star" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Morning Star{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLMORNINGDOJISTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.GREEN + f"Morning Doji Star" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Morning Doji Star{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLEVENINGSTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.FAIL + f"Evening Star" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Evening Star{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLEVENINGDOJISTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.FAIL + f"Evening Doji Star" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Evening Doji Star{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLLADDERBOTTOM(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.GREEN + f"Bullish Ladder Bottom" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bullish Ladder Bottom{existingPattern}"
            else:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.FAIL + f"Bearish Ladder Bottom" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bearish Ladder Bottom{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDL3LINESTRIKE(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.GREEN + f"3 Line Strike" + colorText.END + existingPattern
                )
            else:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.FAIL + f"3 Line Strike" + colorText.END + existingPattern
                )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"3 Line Strike{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDL3BLACKCROWS(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.FAIL + f"3 Black Crows" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"3 Black Crows{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDL3INSIDE(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.GREEN + f"3 Inside Up" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"3 Outside Up{existingPattern}"
            else:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.FAIL + f"3 Inside Down" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"3 Inside Down{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDL3OUTSIDE(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.GREEN + f"3 Outside Up" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"3 Outside Up{existingPattern}"
            else:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.FAIL + f"3 Outside Down" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"3 Outside Down{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDL3WHITESOLDIERS(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.GREEN + f"3 White Soldiers" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"3 White Soldiers{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLHARAMI(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.GREEN + f"Bullish Harami" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bullish Harami{existingPattern}"
            else:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD + colorText.FAIL + f"Bearish Harami" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bearish Harami{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLHARAMICROSS(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD
                    + colorText.GREEN
                    + f"Bullish Harami Cross" + existingPattern
                    + colorText.END
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bullish Harami Cross{existingPattern}"
            else:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD
                    + colorText.FAIL
                    + f"Bearish Harami Cross" + existingPattern
                    + colorText.END
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bearish Harami Cross{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLMARUBOZU(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD
                    + colorText.GREEN
                    + f"Bullish Marubozu" + existingPattern
                    + colorText.END
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bullish Marubozu{existingPattern}"
            else:
                dict["Pattern"] = (
                    colorText.BOLD + colorText.FAIL + f"Bearish Marubozu" + colorText.END + existingPattern
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bearish Marubozu{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLHANGINGMAN(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.FAIL + f"Hanging Man" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Hanging Man{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLHAMMER(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.GREEN + f"Hammer" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Hammer{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLINVERTEDHAMMER(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.GREEN + f"Inverted Hammer" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Inverted Hammer{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLSHOOTINGSTAR(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.FAIL + f"Shooting Star" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Shooting Star{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLDRAGONFLYDOJI(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.GREEN + f"Dragonfly Doji" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Dragonfly Doji{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLGRAVESTONEDOJI(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                colorText.BOLD + colorText.FAIL + f"Gravestone Doji" + colorText.END + existingPattern
            )
            saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Gravestone Doji{existingPattern}"
            hasCandleStickPattern = True

        check = pktalib.CDLENGULFING(
            data["Open"], data["High"], data["Low"], data["Close"]
        )
        if check is not None and check.tail(1).item() != 0:
            if check.tail(1).item() > 0:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD
                    + colorText.GREEN
                    + f"Bullish Engulfing" + existingPattern
                    + colorText.END
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bullish Engulfing{existingPattern}"
            else:
                dict["Pattern"] = (self.findCurrentSavedValue(dict,saveDict,"Pattern")[0] + 
                    colorText.BOLD
                    + colorText.FAIL
                    + f"Bearish Engulfing" + existingPattern
                    + colorText.END
                )
                saveDict["Pattern"] = self.findCurrentSavedValue(dict,saveDict,"Pattern")[1] +  f"Bearish Engulfing{existingPattern}"
            hasCandleStickPattern = True
        if hasCandleStickPattern:
            return True
        return False
