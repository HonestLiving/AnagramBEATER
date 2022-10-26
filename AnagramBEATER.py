import PySimpleGUI as sg

# Find out how to convert this into exe file

sg.theme('DarkAmber')

layout = [  [sg.Text("WELCOME TO ANAGRAM BEATER")],
            [sg.Text("Manual Input:"),sg.InputText()],
            [sg.Button("Read"),sg.Button("Clear")]
         ]

# Create the window
window = sg.Window("ANAGRAM BEATER", layout)

# Create an event loop
while True:
    event, values = window.read()
    print(event,values)
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    print('You entered ', values[0])

window.close()