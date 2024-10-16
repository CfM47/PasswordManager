from utils.dbconfig import dbConfig
from rich import print as printc
from rich.console import Console


console = Console()

def initial_config():  
  db = dbConfig()

initial_config()