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
import pytest
from pkscreener.classes.MenuOptions import menu, menus

class TestMenu:
    def test_create(self):
        m = menu()
        m.create("1", "Test Menu", level=1, isException=False, parent=None)
        assert m.menuKey == "1"
        assert m.menuText == "Test Menu"
        assert m.level == 1
        assert m.isException == False
        assert m.parent == None

    def test_keyTextLabel(self):
        m = menu()
        m.menuKey = "1"
        m.menuText = "Test Menu"
        assert m.keyTextLabel() == "1 > Test Menu"

    def test_commandTextKey(self):
        m = menu()
        m.menuKey = "1"
        m.parent = None
        assert m.commandTextKey() == "/1"
        p = menu()
        p.menuKey = "P"
        m.parent = p
        assert m.commandTextKey() == "/P_1"

    def test_commandTextLabel(self):
        m = menu()
        m.menuText = "Child Menu"
        m.parent = None
        assert m.commandTextLabel() == "Child Menu"
        p = menu()
        p.menuText = "P"
        m.parent = p
        assert m.commandTextLabel() == "P > Child Menu"

    def test_render(self):
        m = menu()
        m.menuKey = "1"
        m.menuText = "Test Menu"
        m.isException = False
        m.hasLeftSibling = False
        assert m.render() == "\n     1 > Test Menu"

    def test_renderSpecial(self):
        m = menu()
        m.menuKey = "T"
        m.level = 0
        assert "Toggle between long-term (Default)" in m.renderSpecial("T")
        m.menuText = "Random"
        m.level = 1
        assert m.renderSpecial("T") == "~"
        assert m.renderSpecial("Whatever") == "~"
        m.level = 0
        assert m.renderSpecial("AnythingOtherThanT") == "~"

class TestMenus:
    def test_fromDictionary(self):
        m = menus()
        rawDictionary = {
            "1": "Menu 1",
            "2": "Menu 2",
            "3": "Menu 3"
        }
        m.fromDictionary(rawDictionary)
        assert len(m.menuDict) == 3
        assert m.find("1").menuText == "Menu 1"
        assert m.find("2").menuText == "Menu 2"
        assert m.find("3").menuText == "Menu 3"

    def test_render(self):
        m = menus()
        rawDictionary = {
            "1": "Menu 1",
            "2": "Menu 2",
            "3": "Menu 3"
        }
        m.fromDictionary(rawDictionary)
        assert m.render() == "\n     1 > Menu 1\n     2 > Menu 2\n     3 > Menu 3"

    def test_find_existing_key(self):
        m = menus()
        rawDictionary = {
            "1": "Menu 1",
            "2": "Menu 2",
            "3": "Menu 3"
        }
        m.fromDictionary(rawDictionary)
        assert m.find("1").menuText == "Menu 1"

    def test_find_nonexistent_key(self):
        m = menus()
        rawDictionary = {
            "1": "Menu 1",
            "2": "Menu 2",
            "3": "Menu 3"
        }
        m.fromDictionary(rawDictionary)
        assert m.find("4") is None
        assert m.find() is None

    def test_renderLevel0Menus(self):
        m = menus()
        rawDictionary = {
            "1": "Menu 1",
            "2": "Menu 2",
            "3": "Menu 3"
        }
        m.fromDictionary(rawDictionary)
        assert m.renderLevel0Menus() == '\n     X > Scanners\n     S > Strategies\n     B > Backtests\n     G > Growth of 10k\n\n     T > Toggle between long-term (Default)\x1b[93m [Current]\x1b[0m and Intraday user configuration\n\n\n     E > Edit user configuration\n     Y > View your user configuration\n\n     U > Check for software update\n     H > Help / About Developer\n     Z > Exit (Ctrl + C)'

    def test_renderForMenu_Lorenzian(self):
        m = menus()
        assert m.renderForMenu() == '\n     X > Scanners\n     S > Strategies\n     B > Backtests\n     G > Growth of 10k\n\n     T > Toggle between long-term (Default)\x1b[93m [Current]\x1b[0m and Intraday user configuration\n\n\n     E > Edit user configuration\n     Y > View your user configuration\n\n     U > Check for software update\n     H > Help / About Developer\n     Z > Exit (Ctrl + C)'
        m1 = m.find("X")
        m1.level = 3
        m1.menuKey = "7"
        list_menus = m.renderForMenu(selectedMenu=m1, asList=True)
        assert len(list_menus) == 4
        assert list_menus[0].menuText == "Buy"
        assert list_menus[1].menuText == "Sell"
        assert list_menus[2].menuText == "Any/All"
    
    def test_renderLevel_X(self):
        m = menus()
        assert m.renderLevel1_X_Menus() is not None
        assert m.renderLevel2_X_Menus() is not None
        assert m.renderLevel3_X_Reversal_Menus() is not None
        assert m.renderLevel3_X_ChartPattern_Menus() is not None
        assert m.renderLevel3_X_PopularStocks_Menus() is not None
        assert m.renderLevel3_X_StockPerformance_Menus() is not None
        assert m.renderLevel4_X_Lorenzian_Menus() is not None
