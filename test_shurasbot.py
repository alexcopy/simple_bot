import unittest
from shurasbot import ShurasBot

class TestShurasBot(unittest.TestCase):
    def test_run_bot(self):
        bot = ShurasBot()
        assert True is True
        bot.run_bot()

if __name__ == "__main__":
    unittest.main()

