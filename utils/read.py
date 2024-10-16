from utils.dbconfig import *
from rich import print as printc
from utils.encription import *
from utils.tools import *

def read(masterKey, name, collectionName):
  db = get_db()
  
  doc = db[collectionName].find_one({"entryName": name})
  if not doc:
    printc(f"[yellow][-][/yellow] Entry with name '{name}' does not exists")
    return
  
  print_document(doc, name)
  
  password = decript_str(doc["password"], get_numeric_key(masterKey))
  copy_to_clipboard(password)
  printc(f"[green]Password copied to clipboard[/green]")
  
def get_account(masterKey, name):
  read(masterKey, name, "accounts")

def get_card(masterKey, name):
  read(masterKey, name, "cards")