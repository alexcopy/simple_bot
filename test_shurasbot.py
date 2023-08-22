import unittest
from shurasbot import ShurasBot

class TestShurasBot(unittest.TestCase):
    def test_run_bot(self):
        bot = ShurasBot()
        bot.run_bot()

if __name__ == "__main__":
    unittest.main()

