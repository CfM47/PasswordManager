from utils.dbconfig import dbConfig
from rich import print as printc
from rich.console import Console


console = Console()

def initial_config():
  # Create database  
  db = dbConfig()
    
  # Create collections    
initial_config()