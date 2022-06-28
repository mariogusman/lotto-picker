import numpy as np


allNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
probability = [0.01617214648, 0.01704089816, 0.01530339481, 0.01784282277, 0.01817695803, 0.0167067629, 0.01577118418, 0.01690724405, 0.01570435712, 0.0190457097, 0.01737503341, 0.01603849238, 0.0169740711, 0.01557070302, 0.0146351243, 0.01730820636, 0.01750868752, 0.01630580059, 0.01577118418, 0.01610531943, 0.01430098904, 0.01470195135, 0.01784282277, 0.01710772521, 0.01583801123, 0.01369954558, 0.01750868752, 0.01757551457, 0.01737503341, 0.01770916867, 0.01577118418, 0.01717455226, 0.01797647688, 0.01750868752, 0.01757551457, 0.01717455226, 0.01811013098, 0.01730820636, 0.01570435712, 0.01603849238, 0.01764234162, 0.01837743919, 0.01730820636, 0.01744186047, 0.01603849238, 0.01663993585, 0.01590483828, 0.01537022187, 0.01724137931, 0.01630580059, 0.01724137931, 0.0167067629, 0.01911253675, 0.01770916867, 0.01410050789, 0.01710772521, 0.01583801123, 0.01617214648, 0.01570435712, 0.01577118418]


# A function to draw 5 numbers from 1 to 60 using the probability distribution of the numbers
def drawNumbers():
    numbers = []
    for i in range(5):
        numbers.append(np.random.choice(allNumbers, p=probability))
        print("Number " + str(i+1) + ": " + str(numbers[i]) + " (" + str(round(probability[numbers[i]-1]*100, 2)) + "%)")
    return numbers


# print the numbers with the text "Seu jogo é: " along with the list of numbers without the [ and ] characters
def printNumbers(numbers):
    print("Seu jogo é: " + str(numbers)[1:-1])


printNumbers(drawNumbers())