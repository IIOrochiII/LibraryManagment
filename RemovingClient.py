import os
import pandas as pd
import csv
def remove_client_by_id(clientid: int):
    def proces_usuwania():
        try:
            os.chdir("DATABASE")
        except FileNotFoundError as e:
            print("You are in incorrect dir",e)
        name = str(clientid) + ".csv"
        try:
            os.remove(name)
        except FileNotFoundError as e:
            print("File is already deleted",e)
        os.chdir("..")
        try:
            df = pd.read_csv("address.csv")
        except FileNotFoundError as e:
            print('Database does not exist',e)
        except ConnectionError as e:
            print("Program couldn't open database",e)
        df.drop(df.index[(df["ID"] == clientid)], axis=0, inplace=True)
        df.to_csv("address.csv", index=False)
        try:
            df = pd.read_csv("customer.csv")
        except FileNotFoundError as e:
            print("File not found",e)
        except ConnectionError as e:
            print("Program couldn't open database", e)
        df.drop(df.index[(df["ID"] == clientid)], axis=0, inplace=True)
        df.to_csv("customer.csv", index=False)
    return proces_usuwania()

def remove_client_by_name(ClientName:str):
                clientID = ""
                try:
                    with open("customer.csv", 'r') as csvfile:
                        fields = ["ID","NAME","E-MAIL","PHONE","CREATED","UPDATED"]
                        reader = csv.DictReader(csvfile, fieldnames=fields)
                        for row in reader:
                            if row['NAME'] == ClientName:
                                clientID = row['ID']
                except FileNotFoundError as e:
                    print('You are in incorrect folder',e)
                name = str(clientID) + ".csv"
                clientID = int(clientID)
                try:
                    df = pd.read_csv("address.csv")
                except FileNotFoundError as e:
                    print("Program was not able to find csv",e)
                except ConnectionError as e:
                    print("Program couldn't open database",e)
                df.drop(df.index[(df["ID"] == clientID)], axis=0, inplace=True)
                df.to_csv("address.csv", index=False)
                try:
                    df = pd.read_csv("customer.csv")
                except FileNotFoundError as e:
                    print("You are in incorrect folder",e)
                except ConnectionError as e:
                    print("Program couldn't open database")
                df.drop(df.index[(df["ID"] == clientID)], axis=0, inplace=True)
                df.to_csv("customer.csv", index=False)
                os.chdir("DATABASE")
                try:
                    os.remove(name)
                except FileNotFoundError as e:
                    print("The csv didn't exist or was already deleted",e)
                os.chdir("..")
