from pymongo import MongoClient, errors
from rich import print as printc
from rich.console import Console
from utils.schemas import *
from utils.encription import *
from getpass import getpass

console = Console()

def dbConfig():
  client = MongoClient("localhost", 27017, serverSelectionTimeoutMS=5000)
  client.admin.command('ping')
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
        
    hash = encript_str(user_name, get_numeric_key(password))
    db["users"].insert_one({ "name": user_name, "hash" : hash })

    db.create_collection("accounts", validator=account_schema)
    db.create_collection("cards", validator=card_schema)
    
  printc("[green][+] Database set up succesfully [/green]")
  return db

def get_db():
  client = MongoClient("localhost", 27017, serverSelectionTimeoutMS=5000)
  client.admin.command('ping')
  db_name = "password-manager"
  return client[db_name]

def check_existence(name, collection):
  entry = collection.find_one({"entryName": name})
  if entry :
    return True
  else :
    return False