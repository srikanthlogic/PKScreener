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
from PKDevTools.classes.PKDateUtilities import PKDateUtilities

class Security:
    def __init__(self, ticker, ):
        self.name = ""
        self.ltp = 0

class Portfolio:
    def __init__(self, name):
        self.name = name
        self.initialValue = 0
        self.currentValue = 0
        self.profit = 0
        self.loss = 0
        self.addedSecuritiesInfo = {}
        self.removedSecuritiesInfo = {}
    
    def addSecurity(self, security:Security=None):
        self.addedSecuritiesInfo[PKDateUtilities.currentDateTime().strftime("%Y-%m-%d")] = {security.name : 1}
        self.initialValue += security.ltp


    def removeSecurity(self, security:Security=None):
        self.removedSecuritiesInfo[PKDateUtilities.currentDateTime().strftime("%Y-%m-%d")] = {security.name : 1}

    def getDifference(self,x):
        return x.iloc[-1] - x.iloc[0]

    def differenceFromLastNTradingSession(self,df,n=1):
        df['LTP'].rolling(window=n).apply(self.getDifference)

