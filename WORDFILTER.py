# This program filters through a txt to find a bunch of 3 to 6 letter words

reader = open('Collins_Scrabble_Words_2019.txt',"r")
writer = open('suitableWords.txt',"w")

try:

    line = reader.readline()
    while line != "":
        # Need strip new line character
        if len(line) >=4 and len(line) <=7 and line.strip().isalpha()==True:

            writer.write(line)

        line = reader.readline()
finally:
    reader.close()
