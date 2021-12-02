import unittest
import requests
import json

from player_height import height_func

data=requests.get("https://mach-eight.uc.r.appspot.com/")
players=json.loads(data.text)['values']

class TestPlayersHeightSumEqualsInput(unittest.TestCase):
    def testFromInstructions(self):
        input = "139"
        result = height_func(players,input)
        data=["- Brevin Knight            Nate Robinson",
              "- Nate Robinson            Mike Wilks"    
            ]
        data2=["- Brevin Knight         Nate Robinson",
               "- Nate Robinson         Mike Wilks"    
            ]

        same=False

        if data==result or data2==result:
            same=True
        self.assertEqual(same, True)

    def testInput0(self):
        input = "0"
        result = height_func(players,input)
        self.assertEqual(result, "Input is 0")
    
    def testInputNotInteger1(self):
        input = "24.3"
        result = height_func(players,input)
        self.assertEqual(result, "Input not Integer")

    def testInputNotInteger2(self):
        input = "hola amigos"
        result = height_func(players,input)
        self.assertEqual(result, "Input not Integer")

    def testVeryLargeNumber(self):
        input = "545104"
        result = height_func(players,input)
        self.assertEqual(result,"No matches found. Try an input smaller than 180 since the most tall player measures 90 inches.")

    def testVerySmallNumber(self):
        input = "1"
        result = height_func(players,input)
        self.assertEqual(result,"No matches found. Try an input larger than 138 since the least tall player measures 69 inches.")
    
    def testInRangeButNotFound(self):
        input = "138"
        result = height_func(players,input)
        self.assertEqual(result,"No matches found")