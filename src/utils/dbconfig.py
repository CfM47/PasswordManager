from pymongo import MongoClient
from rich import print as printc
from rich.console import Console
from schemas import *
from getpass import getpass

console = Console()

def dbConfig():
  try:
    client = MongoClient("localhost", 27017)
    db_name = "password-manager"
    db = client[db_name]
    
    if db_name not in client.list_database_names():
      db.create_collection("users", validator=user_schema)
      user_name = input("Please enter your name: ")
      console.print(f"[bold blue]Welcome, {user_name}![/bold blue] [green]Please enter your password...[/green]")
      
      password = ""
      while True:
        password = getpass("Choose a MASTER PASSWORD: ")
        if password == getpass("Re-type: ") and password!="":
          break
        printc("[yellow][-] Please try again.[/yellow]")

      db.create_collection("accounts", validator=account_schema)
      db.create_collection("cards", validator=card_schema)
    else:
      printc(f"[green]Database '{db_name}' already exists.[/green]")
  except Exception as e:
    console.print_exception(show_locals=True)
    
  printc("[green][+] Database set up succesfully [/green]")
  return db