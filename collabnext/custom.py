
from pyalex import Institutions, Institution
import pandas as pd
import json

def get_institutions_howardu() -> list[Institution]:
    return Institutions().filter(openalex="I137853757").get()

def get_institutions_hbcus(dataloadtype) -> list[Institution]:
    institutions_hbcus = []

    if dataloadtype == "local":
        try:
            institutions_hbcus = json.load(open("data/institutions_hbcus.json"))
        except Exception as e:
            print("Error loading HBCUs JSON data:", e)

    if dataloadtype == "api" or len(institutions_hbcus) == 0:
        try:
            # Read list of HBCUs Names from Eligibility Data
            inst_df = pd.read_csv("data/institutions_hbcus.csv")
            inst_df["query"] = inst_df["name"].str.lower()
            inst_df["query"] = inst_df["query"].str.replace(" &", "")

            # Run API search for HBCUs and add filtered results
            for query in inst_df["query"].tolist():
                institutions_query = Institutions().filter(display_name={"search": query}).get()

                for inst in institutions_query:
                    hbcu_inst_ids = [x["id"] for x in institutions_hbcus]
                    if (inst["display_name"] in inst_df["name"].tolist()) and (inst["id"] not in hbcu_inst_ids):
                        print("Adding institution:", inst["display_name"])
                        institutions_hbcus.append(inst)          
        except Exception as e:
            print("Error reading HBCUs names from CSV and fetching API data:", e)

    return institutions_hbcus
