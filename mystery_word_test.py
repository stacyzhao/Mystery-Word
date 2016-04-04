import unittest
import unittest.mock
from mystery_word import *


word = "banana"
class TestMysteryWord(unittest.TestCase):

    def test_length_of_word(self):
        self.assertEqual(length_of_word(word),[" _ "," _ "," _ "," _ "," _ "," _ "])

    def test_index_in_word(self):
        self.assertEqual(index_in_word("h", "hello"), [0])
        self.assertEqual(index_in_word("a", word), [1,3,5])

    def test_does_letter_match(self):
        self.assertTrue(does_letter_match("a", "calf"))
        self.assertFalse(does_letter_match("b", "placeholder"))

    def test_fill_in_letter(self):
        clue = [" _ "," _ "," _ "," _ "," _ "," _ "]
        self.assertEqual(fill_in_letter("f", clue, word),[" _ "," _ "," _ "," _ "," _ "," _ "])
        self.assertEqual(fill_in_letter("a", clue, word),[" _ ","a"," _ ","a"," _ ","a"])
        self.assertEqual(fill_in_letter("n", clue, word),[" _ ","a","n","a","n","a"])
        self.assertEqual(fill_in_letter("b", clue, word),["b","a","n","a","n","a"])

    def test_validate_input(self):
        guessed_letters = ["a", "d", "e", "g", "f"]
        self.assertFalse(validate_input("aa", guessed_letters))
        self.assertFalse(validate_input("a", guessed_letters))
        self.assertFalse(validate_input("$", guessed_letters))
        self.assertFalse(validate_input("", guessed_letters))
        self.assertTrue(validate_input("b", guessed_letters))

    def test_win_game(self):
        self.assertTrue(win_game("banana", word))
        self.assertFalse(win_game("banaa", word))

    def test_lost_game(self):
        self.assertTrue(lost_game(0, word))
        self.assertFalse(lost_game(4, word))



if __name__ == '__main__':
    unittest.main()
