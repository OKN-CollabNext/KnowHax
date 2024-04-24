from pyalex import Institution, Institutions
import json
import os
import scripts.fetch_custom_institutions as fetch_custom_institutions


def get_institutions(institutions_file_path: str = "observable/docs/data/institutions.json") -> list[Institution]:
    institutions = []
    
    # Load institutions from JSON file
    try:        
        institutions = json.load(open(institutions_file_path))        
    except Exception as e:
        print("\nError loading institutions from JSON file", institutions_file_path, ":", e, "\n")
    
    # Fetch institutions from API if JSON file is empty or not found
    try:
        if institutions is None or len(institutions) == 0:
            print("No institutions found in JSON file, attempting to fetch from the API\n")
            institutions = fetch_custom_institutions.fetch_institutions_from_api(os.getenv("INSTITUTION_FILTER"))
    except Exception as e:
        print("\nError fetching institutions from the API:", e, "\n")

    # Get 5 random institutions in case of error
    if institutions is None or len(institutions) == 0:
        print("No institutions found in JSON file or fetched from the API, fetching random institutions\n")
        institutions = [Institutions().random() for _ in range(5)]
    
    return institutions


if __name__ == "__main__":
    institutions = get_institutions()
    print("Loaded", len(institutions), "institutions\n")
