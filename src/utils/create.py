from dbconfig import *
from rich import print as printc
from rich.console import Console
from getpass import getpass
from encription import *
from tools import copy_to_clipboard
  
def create_account(masterKey, name):
  db = dbConfig()
  
  if check_existence(name, db.accounts):
    printc("[yellow][-][/yellow] Entry with that name already exists")
    return
  siteurl = input("Please enter siteurl: ")
  email = input("Please enter email: ")
  username = input("Please enter username:")
    
  printc("Would you like to enter a password (1) or save a random generated password (2) :")
  while True:
    try:
      option = int(input("Enter 1 or 2: "))
      if option in [1, 2]:
        break
      else:
        printc("[red]Invalid choice, please enter 1 or 2.[/red]")
    except ValueError:
      printc("[red]Invalid input, please enter a number.[/red]")
    
  if option == 1:
      password = getpass("Please enter your password: ")
  else:
      # Aquí puedes generar una contraseña aleatoria
      password = gen_random_password()
  copy_to_clipboard(password)
  
  encrypted_pass = encript_str(password, get_numeric_key(masterKey))
  db.accounts.insert_one({ "entryName": name, "siteurl": siteurl, "username": username, "password" : encrypted_pass})
  # Aquí puedes continuar con el proceso de guardar la cuenta
  printc(f"[green]Account '{name}' added successfully")

def create_card(masterKey, name):
  db = dbConfig()
  
  if check_existence(name, db.cards):
    printc("[yellow][-][/yellow] Entry with that name already exists")
    return
  code = input("Please enter card code: ")
  pin = getpass("Please enter pin: ")
  encrypted_pass = encript_str(pin, get_numeric_key(masterKey))
  db.cards.insert_one({ "entryName": name, "code": code, "password" : encrypted_pass})
  # Aquí puedes continuar con el proceso de guardar la cuenta
  printc(f"[green]Account '{name}' added successfully")