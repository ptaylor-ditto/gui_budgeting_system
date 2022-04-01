from csv import reader
import PySimpleGUI as sg
import random, os, csv

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
home_layout = [
    [sg.Text('Welcome to the Budgeting Program. What would you like to do?')],
    [sg.Button('Login'), sg.Button('Create Account'), sg.Button('Delete Account'), sg.Button('Leave')]
]
login_layout = [
    [sg.Text('Welcome to the Login Screen')],
    [sg.Text('What is the username?'), sg.InputText(key='username')],
    [sg.Text('What is the password?'), sg.InputText(key='password')],
    [sg.Button('Sign in', bind_return_key=True), sg.Button('Leave')]
]
signed_in_layout = [
    [sg.Text('Welcome to the budgeting system.')],
    [sg.Text('What would you like to do?')],
    [sg.Button('View'), sg.Button('Create'), sg.Button('Delete'), sg.Button('Edit'), sg.Button('Leave')]
]
signedin_layout = [
    [sg.Text('Welcome to the budgeting system.')],
    [sg.Text('What would you like to do?')],
    [sg.Button('View'), sg.Button('Create'), sg.Button('Delete'), sg.Button('Edit'), sg.Button('Leave')]
]
signedinlayout = [
    [sg.Text('Welcome to the budgeting system.')],
    [sg.Text('What would you like to do?')],
    [sg.Button('View'), sg.Button('Create'), sg.Button('Delete'), sg.Button('Edit'), sg.Button('Leave')]
]
sign_in = [
    [sg.Text('Welcome to the budgeting system.')],
    [sg.Text('What would you like to do?')],
    [sg.Button('View'), sg.Button('Create'), sg.Button('Delete'), sg.Button('Edit'), sg.Button('Leave')]
]
create_account_layout = [
    [sg.Text('Create account here:')],
    [sg.Text('What is the username?'), sg.InputText(key='username')],
    [sg.Text('What is the password?'), sg.InputText(key='password')],
    [sg.Button('Create Account.', bind_return_key=True), sg.Button('Leave')]
]
delete_account_layout = [
    [sg.Text('Delete account here:')],
    [sg.Text('What is the username?'), sg.InputText(key='username')],
    [sg.Text('What is the password?'), sg.InputText(key='password')],
    [sg.Button('Delete Account.', bind_return_key=True), sg.Button('Leave')]
]
view_layout = [
    [sg.Text('Which budget would you like to view?')],
    [sg.Text(), sg.InputText(key='viewing_budget')],
    [sg.Button('View.', bind_return_key=True), sg.Button('Leave')]
]
create_layout = [
    [sg.Text('Create budget here:')],
    [sg.Text('What is the name of the budget?'), sg.InputText(key='name')],
    [sg.Text('What is the budget amount?'), sg.InputText(key='amount')],
    [sg.Text('How much have you spent so far?'), sg.InputText(key='spent')],
    [sg.Button('Create Budget.', bind_return_key=True), sg.Button('Leave')]
]
delete_layout = [
    [sg.Text('Delete budget here:')],
    [sg.Text('What is the budget name?'), sg.InputText(key='budget')],
    [sg.Text('What is your password?'), sg.InputText(key='password')],
    [sg.Button('Delete Budget', bind_return_key=True), sg.Button('Leave')]
]
edit_layout = [
    [sg.Text('Edit layout here:')],
    [sg.Text('What is the username?'), sg.InputText(key='username')],
    [sg.Text('What is the password?'), sg.InputText(key='password')],
    [sg.Button('Edit Budget.', bind_return_key=True), sg.Button('Leave')]
]
viewing_layout = [
    [sg.Text()]
]
window = sg.Window("Home Page", homepage_layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Leave":
        break
    elif event == "Login":
        window.close()
        window = sg.Window("Login Screen", login_layout)
        current = "Login"
    elif event == "Sign in":
        username = values['username']
        password = values['password']
        if os.path.exists(f"{username}.csv"):
            with open('accounts.csv', 'r') as file:
                read = csv.reader(file, delimiter=',')
                for row in read:
                    if row[0] == username and row[1] == password:
                        cont = 'true'
        if cont == 'true':
            window.close()
            window = sg.Window(f"{username}'s Budgeting Program", signed_in_layout)
            current = "Sign In"
    elif event == "Create Account.":
        username = values['username']
        password = values['password']
        if os.path.exists(f"{username}.csv"):
            continue
        else:
            with open("accounts.csv", 'a', newline=''):
                information = f"{username},{password}"
                file.writelines(information)
                file = open(f"{username}.csv", 'x')
            window.close()
            window = sg.Window("Budgeting Program", signedin_layout)
    elif event == "Delete Account":
        window.close()
        window = sg.Window("Budgeting Program", delete_account_layout)
        current = "Delete Account"
    elif event == "Delete Account.":
        username = values['username']
        contactinfo = []
        file = f"{username}.csv"
        if(os.path.exists(file) and os.path.isfile(file)):
            os.remove(file)
            os.system('cls')
            with open('accounts.csv', 'r') as file:
                file = reader(file)
                for row in file:
                    if row[0] == username:
                        continue
                    else:
                        contactinfo.append(row)
            with open('accounts.csv', 'w') as file:
                file.writelines(contactinfo)
        window.close()
        window = sg.Window("Home Page", home_layout)
    elif event == "Create Account":
        window.close()
        window = sg.Window("Budgeting Program", create_account_layout)
        current = "Create Account"
    elif event == "View":
        window.close()
        window = sg.Window("View Budget", view_layout)
    elif event == "Create":
        window.close()
        window = sg.Window("Create Budget", create_layout)
    elif event == "Create Budget.":
        name = values['name']
        amount = int(values['amount'])
        spent = int(values['spent'])
        left = amount - spent
        file = open(f'{username}.csv', 'a', newline='')
        data = f'{name},{amount},{spent},{left}'
        file.writelines(data)
        window.close()
        window = sg.Window('Budgeting Program', signedinlayout)
    elif event == "Delete":
        window.close()
        window = sg.Window("Delete Budget", delete_layout)
    elif event == "Delete Budget":
        budget = values['budget']
        password = values['password']
        window.close()
        window = sg.Window('Budgeting Program', sign_in)
        addition = []
        with open(f'{username}.csv', 'r') as file:
            file = reader(file)
            for row in file:
                if row[0] == f'{budget}':
                    continue
                else:
                    addition.append(row)
        with open(f'accounts.csv', 'r') as file:
            file = reader(file)
            for row in file:
                if row[0] == username and row[1] == password:
                    continue
                else:
                    break
        with open(f'{username}.csv', 'w') as file:
            file.writelines(addition)
    elif event == "Edit":
        window.close()
        window = sg.Window("Edit Budget", edit_layout)
    elif event == "View.":
        with open(f'{username}.csv', 'r') as file:
            file = reader(file)
            for row in file:
                if row[0] == values['viewing_budget']:
                    viewing_layout[0] == row
        window.close()
        window = sg.Window("Viewing Budget", viewing_layout)
window.close()
