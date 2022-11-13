import PySimpleGUI as sg


# Find out how to convert this into exe file
# In anagrams, there is only 1 duplicate letter at max

sg.theme('DarkAmber')

reader = open('suitableWords.txt',"r")

# Here is a function which update the colomn. aka just closes and opens the window with new data

def columnUpdate():
    #Make window global so we can use it
    global window
    layout = [
              [sg.Text("WELCOME TO ANAGRAM BEATER")],
              [sg.HSeparator()],
              # Gives key of output, place the displayed letters here
              [sg.Text("Selected Letters: "+splitUp), sg.Text(key='-OUTPUT-')],

              [sg.HSeparator()],
              [sg.Text("Enter your letters:"), sg.InputText(key='-IN-')],

              [sg.Button("Read"), sg.Button("Reset")],

              [sg.Text("Answers:", expand_x=True), sg.Column(column, scrollable=True,
                                                             vertical_scroll_only=True, justification='right',
                                                             key="-ANSWERS-")]
              ]
    window.close()
    window = sg.Window("ANAGRAM BEATER", layout,size=(800,500))

def reset():
    #Make window global so we can use it
    global window
    layout = [
              [sg.Text("WELCOME TO ANAGRAM BEATER")],
              [sg.HSeparator()],
              # Gives key of output, place the displayed letters here
              [sg.Text("Selected Letters: "), sg.Text(key='-OUTPUT-')],

              [sg.HSeparator()],
              [sg.Text("Enter your letters:"), sg.InputText(key='-IN-')],

              [sg.Button("Read"), sg.Button("Reset")],

              [sg.Text("Answers:", expand_x=True), sg.Column(column, scrollable=True,
                                                             vertical_scroll_only=True, justification='right',
                                                             key="-ANSWERS-")]
              ]
    window.close()
    window = sg.Window("ANAGRAM BEATER", layout,size=(800,500))

# Correct words array
correctWords = reader.read().splitlines()
for i in range(len(correctWords)):
    correctWords[i]= correctWords[i].upper()

# Stores values for the columnUpdate function
splitUp=""

scrollableAnswersColomn = []

# PySimple stores values in the values array. numbered from 0 to whatever
# use keys instead.
column = []

layout = [  [sg.Text("WELCOME TO ANAGRAM BEATER")],
            [sg.HSeparator()],
            # Gives key of output, place the displayed letters here
            [sg.Text("Selected Letters:"), sg.Text(size=(15,1), key='-OUTPUT-')],

            [sg.HSeparator()],
            [sg.Text("Enter your letters:"),sg.InputText(key= '-IN-')],

            [sg.Button("Read"),sg.Button("Reset")],

            [sg.Text("Answers:",expand_x=True), sg.Column(column, scrollable=True,
                       vertical_scroll_only=True, justification='right', key = "-ANSWERS-")]

         ]

# Create the window
window = sg.Window("ANAGRAM BEATER", layout,size=(800,500))

# Create an event loop
while True:
    # Continuously reads from the window
    event, values = window.read()

    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

    if event == "Read":

        letters = values['-IN-'].upper()
        displayLetters = letters
        splitUp=""

        possibleCombos =[]
        scrollableAnswersColomn =[]
        dupeCheck = []

        # If there are dupes, replace one of the dupes with "-", then after the combos are made replace all "-" with the dupe character
        # Strings are immutable in python. Need cast to array then bring back.
        for i in range(len(letters)):
            if letters[i] not in dupeCheck:
                dupeCheck.append(letters[i])
            else:
                lettersList = list(letters)
                dupeChar = letters[i]
                lettersList[i]="-"
                letters= "".join(lettersList)

        lettersCopy = letters

        for i in range (5):
            # Stores all combos of length i
            temp = []

            # Go through all the characters
            for j in letters:
                for k in lettersCopy:
                    # As long as the character j isnt in k, it is a new combo
                    if j not in k:
                        temp.append (k+j)

                        # only append the combinations of length 3 to 6
                        if len(k+j) >= 3:
                            possibleCombos.append (k+j)
            # Replace combos of prev length with new combos
            lettersCopy = temp

        for i in range(len(possibleCombos)):
            if "-" in possibleCombos[i]:
                tempList = list(possibleCombos[i])
                for j in range(len(tempList)):
                    if tempList[j]=="-":
                        tempList[j]= dupeChar
                possibleCombos[i] = "".join(tempList)

        for i in possibleCombos:
            if i in correctWords:
                scrollableAnswersColomn.append(i)

        noDupeAnswerColomn =[]
        for i in scrollableAnswersColomn:
            if i not in noDupeAnswerColomn:
                noDupeAnswerColomn.append(i)

        # Sorts from greatest to least amount of points
        noDupeAnswerColomn.sort(key=len,reverse=True)

        # This is where to update the characters for the display
        for i in range (len(displayLetters)):
            splitUp+= displayLetters[i]+" "
        window['-OUTPUT-'].update(splitUp)

        # Update column
        column = [
            [sg.Text(noDupeAnswerColomn[i])] for i in range(len(noDupeAnswerColomn))
        ]

        # APPARENTLY THERES NO WAY TO UPDATE FUNCTION FOR COLOMNS
        # SO I HAVE TO CLOSE AND REOPEN THE WINDOW WITH THE UPDATED STUFF. VERY COOL.
        columnUpdate()


    if event == "Reset":
        column=[]
        reset()

window.close()