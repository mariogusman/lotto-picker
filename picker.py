import numpy as np


megaNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
megaProbability = [0.01617214648, 0.01704089816, 0.01530339481, 0.01784282277, 0.01817695803, 0.0167067629, 0.01577118418, 0.01690724405, 0.01570435712, 0.0190457097, 0.01737503341, 0.01603849238, 0.0169740711, 0.01557070302, 0.0146351243, 0.01730820636, 0.01750868752, 0.01630580059, 0.01577118418, 0.01610531943, 0.01430098904, 0.01470195135, 0.01784282277, 0.01710772521, 0.01583801123, 0.01369954558, 0.01750868752, 0.01757551457, 0.01737503341, 0.01770916867, 0.01577118418, 0.01717455226, 0.01797647688, 0.01750868752, 0.01757551457, 0.01717455226, 0.01811013098, 0.01730820636, 0.01570435712, 0.01603849238, 0.01764234162, 0.01837743919, 0.01730820636, 0.01744186047, 0.01603849238, 0.01663993585, 0.01590483828, 0.01537022187, 0.01724137931, 0.01630580059, 0.01724137931, 0.0167067629, 0.01911253675, 0.01770916867, 0.01410050789, 0.01710772521, 0.01583801123, 0.01617214648, 0.01570435712, 0.01577118418]


lotoNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25]
lotoProbability = [0.0397736164, 0.03979969746, 0.0402952376, 0.04008658912, 0.04052996714, 0.03893902248, 0.03857388764, 0.0383391581, 0.03979969746, 0.04139064212, 0.04133848, 0.03985185958, 0.03946064368, 0.04092118304, 0.04073861562, 0.03940848156, 0.03841740128, 0.03969537322, 0.03993010276, 0.03998226488, 0.04144280424, 0.0395128058, 0.03993010276, 0.04079077774, 0.04105158834]


# A function to draw 5 numbers from 1 to 60 using the probability distribution of the numbers and making sure they are not repeated and sorting the list
def drawMegaNumbersUnique():
    megaDrawnNumbers = []
    print("Mega-Sena:\n")
    for i in range(6):
        megaDrawnNumbers.append(np.random.choice(megaNumbers, p=megaProbability))
        print("Number " + str(i+1) + ": " + str(megaDrawnNumbers[i]) + " (" + str(round(megaProbability[megaDrawnNumbers[i]-1]*100, 2)) + "%)")
    megaDrawnNumbers = list(set(megaDrawnNumbers))
    megaDrawnNumbers.sort()
    return megaDrawnNumbers


# A function to draw 5 numbers from 1 to 25 using the probability distribution of the numbers and making sure they are not repeated and sorting the list
def drawLotoNumbersUnique():
    lotoDrawnNumbers = []
    print("Loto Fácil:\n")
    for i in range(15):
        lotoDrawnNumbers.append(np.random.choice(lotoNumbers, p=lotoProbability))
        print("Number " + str(i+1) + ": " + str(lotoDrawnNumbers[i]) + " (" + str(round(lotoProbability[lotoDrawnNumbers[i]-1]*100, 2)) + "%)")
    lotoDrawnNumbers = list(set(lotoDrawnNumbers))
    lotoDrawnNumbers.sort()
    return lotoDrawnNumbers


# print the numbers with the text "Seu jogo é: " along with the list of numbers without the [ and ] characters
#delimiter
delim = "\n----------------------------------------------------\n"
def printMegaNumbersUnique(megaDrawnNumbers):
    print("\nSeu jogo é: " + str(megaDrawnNumbers)[1:-1] + delim)


def printLotoNumbersUnique(lotoDrawnNumbers):
    print("\nSeu jogo é: " + str(lotoDrawnNumbers)[1:-1] + delim)


printMegaNumbersUnique(drawMegaNumbersUnique())
printLotoNumbersUnique(drawLotoNumbersUnique())