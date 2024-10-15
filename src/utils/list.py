
from dbconfig import *
from rich import print as printc
from encription import *
from tools import *

def list_entries(collectionName):
  db = dbConfig()
  entries = db[collectionName].find()
  for entry in entries:
    print_document(entry, entry["entryName"])
    
def list_names(collectionName):
  db = dbConfig()
  entries = db[collectionName].find()
  for entry in entries:
    printc(f"[green]{entry['entryName']}[/green]")

def list_accounts():
  list_entries("accounts")

def list_cards():
  list_entries("cards")
  
def list_account_names():
  list_names("accounts")

def list_card_names():
  list_names("cards")
  
def list_all():
  list_accounts()
  list_cards()

def list_all_names():
  list_account_names()
  list_card_names()