import PySimpleGUI as sg
import random, os

# username = values["username"]
# print(username)

sg.LOOK_AND_FEEL_TABLE['Theming'] = {
    'BACKGROUND': '#f4ffbd',
    'TEXT': '#000000',
    'INPUT': '#ababab',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#000000',
    'BUTTON': ('#ffffff', '#ff0000'),
    'PROGRESS': ('#D1826B', '#CC8019'),
    'BORDER': 1, 'SLIDER_DEPTH': 0, 
    'PROGRESS_DEPTH': 0,
}
file = open("accounts.csv", 'a')
username = ""
password = ""
themes = ["HotDogStand", "Theming", 'SystemDefault']
sg.theme(random.choice(themes))
homepage_layout = [
    [sg.Text('Welcome to the Budgeting Program. What would you like to do?')],
    [sg.Button('Login'), sg.Button('Create Account'), sg.Button('Delete Account'), sg.Button('Leave')]
]
login_layout = [
    [sg.Text('Welcome to the Login Screen')],
    [sg.Text('What is the username?'), sg.InputText(key='username')],
    [sg.Text('What is the password?'), sg.InputText(key='password')],
    [sg.Button('Sign in'), sg.Button('Leave')]
]
signed_in_layout = [
    [sg.Text('Welcome to the budgeting system.')],
    [sg.Text('What would you like to do?')],
    [sg.Button('Search'), sg.Button('Create'), sg.Button('Delete'), sg.Button('Edit'), sg.Button('Leave')]
]
create_account_layout = [
    [sg.Text('Create account here:')],
    [sg.Text('What is the username?'), sg.InputText(key='username')],
    [sg.Text('What is the password?'), sg.InputText(key='password')],
    [sg.Button('Create Account.'), sg.Button('Leave')]
]
delete_account_layout = [
    [sg.Text('Delete account here:')],
    [sg.Text('What is the username?'), sg.InputText(key='username')],
    [sg.Text('What is the password?'), sg.InputText(key='password')],
    [sg.Button('Delete Account.'), sg.Button('Leave')]
]

window = sg.Window("Home Page", homepage_layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Leave":
        break
    if event == "Login":
        window.close()
        window = sg.Window("Login Screen", login_layout)
        current = "Login"
    elif event == "Sign in":
        window.close()
        if os.path.exists(f"{username}_____.csv"):
            window = sg.Window("Budgeting Program", signed_in_layout)
            current = "Sign In"
        else:
            print(username)
    elif event == "Delete Account":
        window.close()
        window = sg.Window("Budgeting Program", delete_account_layout)
        current = "Delete Account"
    elif event == "Create Account":
        window.close()
        window = sg.Window("Budgeting Program", create_account_layout)
        current = "Create Account"
    elif event == "Create Account.":
        window.close()
        window = sg.Window("Budgeting Program", signed_in_layout)
        username = values['username']
        password = values['password']
        if os.path.exists(f"{username}_____.csv"):
            continue
        else:
            file = open("accounts.csv", 'a', newline='')
            information = f"{username},{password}"
            file.writelines(information)
            file = open(f"{username}_____.csv", 'x')
    elif event == "Delete Account":
        window.close()
        window = sg.Window("Delete Account Screen", delete_account_layout)
window.close()
