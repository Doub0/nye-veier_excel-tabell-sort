# hovedscript.py

import pandas as pd
import funksjoner
from funksjoner import hentKjoretoyData

def vis_excel_innhold():
    """Fetch and display vehicle data from the external module."""
    hentKjoretoyData()

def main():
    """Main function to read Excel data and display it."""
    # File path to the Excel document
    filsti = 'Prosjekter.xlsx'
    
    try:
        # Open the Excel document and read the specified sheet into a DataFrame
        excel_data = pd.read_excel(filsti, sheet_name='ProsjektData')  # Adjust `sheet_name` if necessary
        df = excel_data  # Directly assign the DataFrame
        
        # Print the DataFrame content
        #print(df)
        
        # Display vehicle data
        vis_excel_innhold()
    
    except FileNotFoundError:
        print(f"Eror: The file '{filsti}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Check if this script is running as the main script
if __name__ == '__main__':
    main()