import tkinter as tk
from utils.dbconfig import *
from rich import print as printc
from rich.json import JSON
from utils.encription import *
import json

def copy_to_clipboard(text):
  r = tk.Tk()
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(text)
  r.update()
  r.destroy()
  
def print_document(doc, name):
  doc_copy = doc.copy()
  del doc_copy["_id"]
  del doc_copy["password"]
  
  doc_json_str = json.dumps(doc_copy, indent=2)
  printc(f"[green]Details of '{name}':[/green]")
  printc(JSON(doc_json_str))