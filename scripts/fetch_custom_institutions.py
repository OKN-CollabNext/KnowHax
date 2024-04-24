
from pyalex import Institutions, Institution
import pandas as pd
import json
import os
import sys


def fetch_institutions_from_api(
        institution_filter: str,
        institutions_names_list_path: str = "scripts/hbcus_names_list.csv",
        save_to_file: bool = True,
        institutions_save_path: str = "observable/docs/data/institutions.json"
) -> list[Institution]:
    """
    Fetch institutions from the OpenAlex API based on the specified filter and save the data to a JSON file

    Args:
        institution_filter (str): The filter to determine which institutions to fetch from the API
        institutions_names_list_path (str): CSV file path containing the list of HBCUs names
        save_to_file (bool): Whether to save the institutions data to a JSON file
        institutions_save_path (str): JSON file path to save the institutions data to
    
    Returns:
        list[Institution]: The list of institutions fetched from the API
    """

    institutions = []

    try:
        if institution_filter == "howardu":
            # Fetch Howard University based on OpenAlex ID
            institutions = Institutions().filter(openalex="I137853757").get()
            print("\nFetched institution data for Howard University")
        
        elif institution_filter == "hbcus":

            # Read list of HBCUs Names from Eligibility Data
            inst_df = pd.read_csv(institutions_names_list_path)
            print("\nLoaded list of HBCUs names from:", institutions_names_list_path, "\n")
            inst_df["query"] = inst_df["name"].str.lower()
            inst_df["query"] = inst_df["query"].str.replace(" &", "")

            # Run API search for each HBCU name
            for query in inst_df["query"].tolist():
                institutions_query = Institutions().filter(display_name={"search": query}).get()

                # Check search results for name matches and add to institutions list if not already present
                for inst in institutions_query:
                    hbcu_inst_ids = [x["id"] for x in institutions]
                    if (inst["display_name"] in inst_df["name"].tolist()) and (inst["id"] not in hbcu_inst_ids):
                        print("Adding institution:", inst["display_name"])
                        institutions.append(inst)
            
            print("\nFetched data for", len(institutions), "out of", inst_df.shape[0], "institutions\n")
        
        else:
            print("Invalid value of INSTITUTION_FILTER, make sure to set it to 'hbcus' or 'howardu' (without the quotes) in your .env file")
        
        # Save institutions data to JSON file if required
        if (save_to_file) and (len(institutions) > 0):            
            with open(institutions_save_path, "w") as f:
                json.dump(institutions, f)
                print("Institutions data saved to", institutions_save_path, "\n")

    except Exception as e:
        print("\nError fetching institutions from the API:", e, "\n")
    
    return institutions


if __name__ == "__main__":
    
    institution_filter = os.getenv("INSTITUTION_FILTER")

    if sys.argv[1] and sys.argv[1] in ["howardu", "hbcus"]:
        institution_filter = sys.argv[1]
    
    institutions = fetch_institutions_from_api(institution_filter)
    print("Completed fetching institutions data from the OpenAlex API\n")
