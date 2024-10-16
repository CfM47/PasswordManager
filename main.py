import argparse
from rich import print as printc
from utils.dbconfig import get_db
from utils.encription import *
from utils.create import *
from utils.read import *
from utils.delete import *
from utils.list import *


parser = argparse.ArgumentParser(description='Description')

parser.add_argument('option', help='(c)reate / (r)ead / (d)elete / (l)ist / list-(d)etails')
parser.add_argument('type', help='account / card  / all')
parser.add_argument("-n", "--name", help="Name", required=False)

args = parser.parse_args()

def validateMasterKey(masterKey):
  db = get_db()
  user = db["users"].find_one()
  if not user :
    printc("[red] - [/red] You have'nt set a master password. Run config.py first")
    return
  name = user["name"]
  hash = user["hash"]
  nameHash = encript_str(name, get_numeric_key(masterKey))
  return hash == nameHash

def get_validate_password():
  password = getpass("Enter your password:")
  if validateMasterKey(password):
    return password
  printc("[red][!][/red] Incorrect password")
  return ""

def handle_create_read(actions):
  if args.type == None:
    printc("[red][!][/red] Type (account / card) required ")
    return
  if not (args.type in ["account", "card"]):
    printc("[red][!][/red] Invalid value for type")
  if args.name == None:
    printc("[red][!][/red] Entry Name (-n) required ")
    return
    
  masterKey = get_validate_password()
  if len(masterKey) == 0:
    return
  
  actions[args.type](masterKey, args.name)

def handle_delete(actions):
  if args.name == None:
    printc("[red][!][/red] Entry Name (-n) required ")
    return
  if not (args.type in ["account", "card"]):
    printc("[red][!][/red] Invalid value for type")
    return
  masterKey = get_validate_password()
  if len(masterKey) == 0:
    return
  actions[args.type](args.name)
  
def handle_list(actions):  
  if args.type == None:
    printc("[red][!][/red] Type (account / card / all) required ")
    return
  if not (args.type in ["account", "card", "all"]):
    printc("[red][!][/red] Invalid value for type")
    return
  validateMasterKey = get_validate_password()
  if len(validateMasterKey) == 0:
    return
  
  actions[args.type]()
  printc(f"[blue]Entries listed succesfully[/blue]")

def handle_details(actions):
  if args.type == None:
    printc("[red][!][/red] Type (account / card / all) required ")
    return
  if not (args.type in ["account", "card", "all"]):
    printc("[red][!][/red] Invalid value for type")
    return
  validateMasterKey = get_validate_password()
  if len(validateMasterKey) == 0:
    return
  
  actions[args.type]()
  printc(f"[blue]Entries listed succesfully[/blue]")

def main():
  if args.option in ["create","c"]:
    handle_create_read({
      "account": create_account,
      "card" : create_card,
    })
    return
  if args.option in ["read", "r"]:
    handle_create_read({
      "account": get_account,
      "card" : get_card,
    })
    return
  if args.option in ["delete", "d"]:
    handle_delete({
      "account": delete_account,
      "card" : delete_card,
    })
    return
  if args.option in ["list", "l"]:
    handle_list({
      "account": list_account_names,
      "card": list_card_names,
      "all": list_all_names,
    })
  if args.option in ["list-details", "d"]:
    handle_details({
      "account": list_accounts,
      "card": list_cards,
      "all": list_all,
    })
    
main()
