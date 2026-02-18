from data_layer.db_context import DbContext
from Services.authenticater_service import Authenticater
from UI.cli import CLI

 
def main():
    db = DbContext()
    auth = Authenticater(db)
    cli = CLI(auth)
    cli.menu()

            

if __name__ == "__main__":
        main()