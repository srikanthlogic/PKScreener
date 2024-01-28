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

    def test_commandTextLabel(self):
        m = menu()
        m.menuText = "Test Menu"
        m.parent = None
        assert m.commandTextLabel() == "Test Menu"

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

    def test_renderLevel0Menus(self):
        m = menus()
        rawDictionary = {
            "1": "Menu 1",
            "2": "Menu 2",
            "3": "Menu 3"
        }
        m.fromDictionary(rawDictionary)
        assert m.renderLevel0Menus() == '\n     X > Scanners\n     S > Strategies\n     B > Backtests\n     G > Growth of 10k\n\n     T > Toggle between long-term (Default)\x1b[93m [Current]\x1b[0m and Intraday user configuration\n\n\n     E > Edit user configuration\n     Y > View your user configuration\n\n     U > Check for software update\n     H > Help / About Developer\n     Z > Exit (Ctrl + C)'
