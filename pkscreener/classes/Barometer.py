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

import asyncio
import os
import datetime
from PIL import Image,ImageDraw,ImageFont
try:
    from pyppeteer import launch
except:
    pass
from PKDevTools.classes import Archiver
from pkscreener.classes import Utility
from pkscreener.classes.MarketStatus import MarketStatus

async def getScreenshotsForGlobalMarketBarometer():
    # https://scrapeops.io/python-web-scraping-playbook/python-pyppeteer/#how-to-click-on-buttons-with-pyppeteer
    folderPath = Archiver.get_user_outputs_dir()
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.morningstar.com/markets/global-market-view',timeout=10000, waitUntil=['load','domcontentloaded','networkidle0'])
    # Get the latest date for which this GMB is being loaded
    dateElement = await page.querySelector(selector='.date-label')
    date = await page.evaluate('(dateElement) => dateElement.textContent', dateElement)
    await page.waitFor(selectorOrFunctionOrTimeout=2000)
    # Show the india hover tooltip. If you don't do this, the screenshot if only 50% of the map
    await page.hover(selector='.country-India')
    hoverElement = await page.querySelector(selector='.mbc-chart-tooltip-container')
    await page.evaluate('(hoverElement) => hoverElement.innerHTML=hoverElement.innerHTML.replaceAll("Morningstar","").replaceAll("GR INR","Performance")', hoverElement)

    # Hide the india tooltip. This will force the map to appear properly for screenshot
    # await page.hover(selector='.date-label')
    # Take the screenshot
    await page.screenshot({'path': os.path.join(folderPath,'gmbstat.png'), 'clip': {"x":50,"y":440,"width":710,"height":460}})

    # Let's find the valuation of the market
    btnValuation = await page.querySelector(selector='button#valuation')
    await page.evaluate('(btnValuation) => btnValuation.click()', btnValuation)
    await page.waitForSelector(selector='.country-India')
    await page.waitFor(selectorOrFunctionOrTimeout=2000)
    await page.hover(selector='.country-India')
    await page.evaluate('(hoverElement) => hoverElement.innerHTML=hoverElement.innerHTML.replaceAll("Morningstar","").replaceAll("GR INR","Valuation")', hoverElement)
    await page.screenshot({'path': os.path.join(folderPath,'gmbvaluation.png'), 'clip': {"x":45,"y":420,"width":710,"height":450}})
    await browser.close()

def getGlobalMarketBarometerValuation():
    try:
        asyncio.get_event_loop().run_until_complete(getScreenshotsForGlobalMarketBarometer())
    except:
        pass
    folderPath = Archiver.get_user_outputs_dir()
    gmbPath = None
    try:
        gapHeight = 65
        bgColor = (0,0,0)
        fontPath = Utility.tools.setupReportFont()
        artfont = ImageFont.truetype(fontPath, 12)
        gmbPerformance = Image.open(os.path.join(folderPath,'gmbstat.png')) # 710 x 460
        gmbValuation = Image.open(os.path.join(folderPath,'gmbvaluation.png')) # 710 x 450
        gmbPerf_size = gmbPerformance.size
        gmbValue_size = gmbValuation.size
        # watermark = Utility.tools.getWatermarkImage(gmbPerformance)
        gmbPerformance = Utility.tools.addQuickWatermark(gmbPerformance, dataSrc="Morningstar, Inc")
        gmbValuation = Utility.tools.addQuickWatermark(gmbValuation, dataSrc="Morningstar, Inc")
        gmbCombined = Image.new('RGB',(gmbPerf_size[0], gmbPerf_size[1]+gmbValue_size[1]+gapHeight), bgColor)
        gmbCombined.paste(gmbPerformance,(0,0))
        draw = ImageDraw.Draw(gmbCombined)
        # artwork
        nseMarketStatus = MarketStatus().getMarketStatus(exchangeSymbol="^NSEI",namedOnly=True)
        bseMarketStatus = MarketStatus().getMarketStatus(exchangeSymbol="^BSESN",namedOnly=True)
        nasdaqMarketStatus = MarketStatus().getMarketStatus(exchangeSymbol="^IXIC")
        repoText = f'https://GitHub.com/pkjmesra/pkscreener/ | © {datetime.date.today().year} pkjmesra | https://t.me/PKScreener\n{nseMarketStatus}\n{bseMarketStatus}\n{nasdaqMarketStatus}'
        draw.text((5, gmbPerf_size[1]+5), Utility.tools.removeAllColorStyles(repoText), font=artfont, fill="lightgreen")
        gmbCombined.paste(gmbValuation,(0,gmbPerf_size[1]+gapHeight))
        gmbCombined.save(os.path.join(folderPath,"gmb.png"),"PNG")
        gmbPath = os.path.join(folderPath,"gmb.png")
        # gmbCombined.show()
    except: #Exception as e:
        # print(e)
        pass
    return gmbPath

