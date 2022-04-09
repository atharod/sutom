# Tusmo

The code is inspired by the famous french game named MOTUS where the goal is to guess a word.
Only the length of this word and its first letter are given.
When a word is given, each letter get a color :
- RED : The letter is at the place (good_ones in the code).
- YELLOW : The letter is present in the searched word but in another position (almost_ones in the code).
- BLUE : The letter does not belong to the searched word (bad_ones in the code).

The code works like this :
- Requests are made to the online dictionnary "https://www.le-dictionnaire.com/" according to the first letter asked. Each webpage provides a list of word.
- This list is then shrinked with the different conditions (RED, YELLOW or BLUE) and length of the word.
- the "while" loop in debroussailleur function allows to input new conditions to the same list without reapeating the requests.

This code is not made for cheating to anything but for personal use only.
