#!/usr/bin/python3
#This was created by me in 2015, and im uploading now because im so nostalgic

import random

winpl1 = 0
winpl2 = 0

aleatorio = random.randint(0,2)

while (winpl1 != 1 and winpl2 != 1):
    print ("Do you want Paper, Rock or Scissors?")
    pl1 = str(input("> "))
    if aleatorio == 0:
        pl2 = "Paper"
    if aleatorio == 1:
        pl2 = "Rock"
    if aleatorio == 2:
        pl2 = "Scissors"

    print ("Computer choices: \n\n", pl2)
    if (pl1 == "Rock" and pl2 == "Scissors"):
        print ("\nPlayer 1 won, rock smashs scissors!")
        winpl1 = winpl1 + 1
    if (pl1 == "Scissors" and pl2 == "Rock"):
        print ("\nPlayer 2 won, rock smashs scissors!")
        winpl2 = winpl2 + 1
    if (pl1 == "Scissors" and pl2 == "Paper"):
        print ("\nPlayer 1 won, scissors cut papers!")
        winpl1 = winpl1 + 1
    if (pl1 == "Paper" and pl2 == "Scissors"):
        print ("\nPlayer 2 won, scissors cut papers!")
        winpl2 = winpl2 + 1
    if (pl1 == "Paper" and pl2 == "Rock"):
        print ("\nPlayer 1 won, paper wons against rock!")
        winpl1 = winpl1 + 1
    if (pl1 == "Rock" and pl2 == "Paper"):
        print ("\nPlayer 2 won, paper wons aginst rock!")
        winpl2 = winpl2 + 1
    if (pl1 == pl2):
        print ("Draw!")
        winpl1 = winpl1 + 1

        
print ("Vencedor: \n\n")

if (winpl1 > winpl2):
    print ("player 1")
else:
    print ("player 2")
