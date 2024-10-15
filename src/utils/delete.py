from utils.dbconfig import *
from rich import print as printc
from utils.encription import *
from utils.tools import *

def delete_entry(name, collectionName):
  db = get_db()
  entry = db[collectionName].find_one({"entryName": name})
  if not entry:
    printc(f"[yellow][-][/yellow] Entry with name '{name}' does not exists")
    return
  
  print_document(entry, name)
  confirm = input("Are you sure you want to delete this entry? (y/n): ")
  if confirm.lower() == "y":
    db[collectionName].delete_one({"entryName": name})
    printc(f"[green]Entry '{name}' deleted successfully[/green]")
  else:
    printc(f"[yellow][-][/yellow] Deletion of entry '{name}' cancelled")
    
def delete_account(name):
  delete_entry(name, "accounts")

def delete_card(name):
  delete_entry(name, "cards")
