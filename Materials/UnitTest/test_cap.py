import unittest
import cap

class TestCap(unittest.TestCase):
    def Test_One_Word(self):
        text = 'one'
        result = cap.cap_text(text)
        self.assertEqual(result, 'One')

    def Test_Two_Words(self):
        text = "two words"
        result = cap.cap_text(text)
        self.assertEqual(result, 'Two Words')

if __name__ == '__main__':
    unittest.main()
