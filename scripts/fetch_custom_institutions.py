
from pyalex import Institutions, Institution
import pandas as pd
import json
import os
import sys


def fetch_institutions_from_api(
        institutions_fetch_filter: str = "hbcus",
        institutions_fetch_count: int = 5,
        institutions_names_list_path: str = "scripts/hbcus_names_list.csv",
        save_to_file: bool = True,
        institutions_save_path: str = "observable/docs/data/institutions.json"
) -> list[Institution]:
    """
    Fetch institutions from the OpenAlex API based on the specified filter and save the data to a JSON file

    Args:
        institutions_fetch_filter (str): The filter to determine which institutions to fetch from the API
        institutions_fetch_count (int): The number of institutions for which to fetch data
        institutions_names_list_path (str): CSV file path containing the list of HBCUs names
        save_to_file (bool): Whether to save the institutions data to a JSON file
        institutions_save_path (str): JSON file path to save the institutions data to
    
    Returns:
        list[Institution]: The list of institutions fetched from the API
    """

    institutions = []

    try:
        if institutions_fetch_filter == "howardu":
            # Fetch Howard University based on OpenAlex ID
            institutions = Institutions().filter(openalex="I137853757").get()
            print("\nFetched institution data for Howard University")
        
        elif institutions_fetch_filter == "hbcus":

            # Read list of HBCUs Names from Eligibility Data
            inst_df = pd.read_csv(institutions_names_list_path)
            print("\nLoaded list of HBCUs names from:", institutions_names_list_path, "\n")
            inst_df["query"] = inst_df["name"].str.lower()
            inst_df["query"] = inst_df["query"].str.replace(" &", "")

            # Run API search for each HBCU name
            hbcu_inst_ids = []
            hbcu_inst_count = 0
            for query in inst_df["query"].tolist():
                # Break if the required number of institutions have been fetched, else proceed with search query
                if hbcu_inst_count >= institutions_fetch_count:
                    break                
                institutions_query = Institutions().filter(display_name={"search": query}).get()

                # Check search results for name matches and add to institutions list if not already present
                for inst in institutions_query:
                    if (inst["display_name"] in inst_df["name"].tolist()) and (inst["id"] not in hbcu_inst_ids) and (hbcu_inst_count < institutions_fetch_count):
                        print("Adding institution:", inst["display_name"])
                        institutions.append(inst)
                        hbcu_inst_ids.append(inst["id"])
                        hbcu_inst_count += 1
            
            print("\nFetched data for", len(institutions), "out of", inst_df.shape[0], "institutions\n")
        
        else:
            print("Invalid value of institutions_fetch_filter, make sure to set it to 'hbcus' or 'howardu' (without the quotes) in your .env file")
        
        # Save institutions data to JSON file if required
        if (save_to_file) and (len(institutions) > 0):            
            with open(institutions_save_path, "w") as f:
                json.dump(institutions, f)
                print("Institutions data saved to", institutions_save_path, "\n")

    except Exception as e:
        print("\nError fetching institutions from the API:", e, "\n")
    
    return institutions


if __name__ == "__main__":

    # Check system arguments and environment variables for filter and count of institutions to fetch
    try:
        institutions_fetch_filter = str(sys.argv[1])
        institutions_fetch_count = int(sys.argv[2])
    except Exception as e:
        print("\nError parsing system arguments:", e, "\n")
        try:
            institutions_fetch_filter = os.getenv("INSTITUTIONS_FETCH_FILTER")
            institutions_fetch_count = int(os.getenv("INSTITUTIONS_FETCH_COUNT"))
        except Exception as e:
            print("\nError fetching environment variables:", e, "\n")
            institutions_fetch_filter = "hbcus"
            institutions_fetch_count = 5
    if institutions_fetch_count is None or institutions_fetch_count <= 0:
        institutions_fetch_count = 5
    
    # Make the API call to fetch data
    institutions = fetch_institutions_from_api(institutions_fetch_filter, institutions_fetch_count)
    print("Completed fetching institutions data from the OpenAlex API\n")
