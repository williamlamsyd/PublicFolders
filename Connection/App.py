import yaml
import os
import pymssql
import sqlalchemy
import getpass
import smtplib
import sys
import os

# ----------------------------------------------------------------------------------------------

# ================= #
# === FUNCTIONS === #
# ================= #

class Transfer:
    
    def __init__(self):
        self.load_config()

    def load_config(self):
        with open("config.yaml", "r") as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("Error when reading config", exc)
                exit()

        self.working_dir = os.path.abspath(self.config['folders']['folder_root'])

    def working_filepath(self, filename):
        return os.path.join(self.working_dir,filename)

    def database_connection(self):
        try:
            self.password = getpass.getpass(prompt=("Enter server password:"),stream=None)
        except Exception as e:
            print("error", e)
        else:
            print('Password accepted')
            self.database_connection = sqlalchemy.create_engine(f"mssql+pymssql://{self.config['destination']['user']}:{self.password}@{self.config['destination']['server']}/{self.config['destination']['database']}")
            return self.database_connection
    


