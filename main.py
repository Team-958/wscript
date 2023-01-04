from bs4 import BeautifulSoup
import requests
from colorama import init
from termcolor import colored
import os
init()

print(colored("===", "blue"), colored("WST script", "cyan"), colored("===\n", "blue"))
print(colored("[1]", "magenta"), colored("Get website", "white"))
print(colored("[2]", "magenta"), colored("Get website text only\n", "white"))
print(colored("===", "blue"), colored("White SecurityTeam", "cyan"), colored("===\n\n", "blue"))

command_1 = ["1"]
command_2 = ["2"]

while True:
            inpt = input(colored("$: enter the number: ", "green"))
            inpt = inpt.strip()
            if inpt in command_1:
                url_1 = input(colored("$: site url: ", "green"))
                print(colored("\n\n===", "magenta"), colored("Analyzing...", "white"), colored("===\n\n", "magenta"))
                response = requests.get(url_1)
                soup = BeautifulSoup(response.text, 'html.parser')

                print(colored(soup.find(), "green"))

                print(colored("\n\n===", "magenta"), colored("Success!", "green"), colored("===\n\n", "magenta"))

            elif inpt in command_2:
                url_1 = input(colored("$: site url: ", "green"))
                print(colored("\n\n===", "magenta"), colored("Analyzing...", "white"), colored("===\n\n", "magenta"))
                response = requests.get(url_1)
                soup = BeautifulSoup(response.text, 'html.parser')

                print(colored(soup.find().get_text(), "green"))

                print(colored("\n\n===", "magenta"), colored("Success!", "green"), colored("===\n\n", "magenta"))

            elif inpt == "cls":
                os.system("cls")
                print(colored("===", "blue"), colored("WST script", "cyan"), colored("===\n", "blue"))
                print(colored("[1]", "magenta"), colored("Get website", "white"))
                print(colored("[2]", "magenta"), colored("Get website text only\n", "white"))
                print(colored("===", "blue"), colored("White SecurityTeam", "cyan"), colored("===\n\n", "blue"))

            elif inpt == "clear":
                os.system("clear ")
                print(colored("===", "blue"), colored("WST script", "cyan"), colored("===\n", "blue"))
                print(colored("[1]", "magenta"), colored("Get website", "white"))
                print(colored("[2]", "magenta"), colored("Get website text only\n", "white"))
                print(colored("===", "blue"), colored("White SecurityTeam", "cyan"), colored("===\n\n", "blue"))

