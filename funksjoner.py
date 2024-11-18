import pandas as pd

def hentKjoretoyData():
    print("Funksjoner funker!")
    
    # File path to the Excel document
    filsti = 'Prosjekter.xlsx'
    
    # Open the Excel document and read the specified sheet into a DataFrame
    excel_data = pd.read_excel(filsti, sheet_name='ProsjektData')  # Adjust `sheet_name` if necessary

    # Get the DataFrame
    df = excel_data[excel_data.keys()]  # Fetch the table if specified as a named table

    # Sort the DataFramex   
    sorted_df = df.sort_values(["min (lette) - alt0","Prosjekter"])

    # Calculate the new column width based on the current display options
    current_width = pd.get_option('display.max_colwidth')
    new_width = int(current_width * 2.005)  # Increase column width by 0.5%

    pd.set_option('display.max_colwidth', new_width)

    current_rows = pd.get_option('display.max_rows')
    new_rows = int(current_rows * 5)  # Increase row display limit by 50%
    pd.set_option('display.max_rows', new_rows)

    repeated_df_vertical = pd.concat([sorted_df] * 5, ignore_index=True)  # Repeat 3 times

    # Print the repeated DataFrame
    print(repeated_df_vertical)

    return repeated_df_vertical
    # Print the sorted DataFrame
    print(sorted_df)

    return sorted_df

    pd.merge(repeated_df_vertical, sorted_df)