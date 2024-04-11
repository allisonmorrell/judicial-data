import pandas as pd
import re
from pathlib import Path

def merge_csv_files(input_directory_path, output_directory_path):
    pattern = r"_(\d{4})\.csv"
    merged_data = pd.DataFrame()

    # Ensure the directory paths are Path objects
    input_directory_path = Path(input_directory_path)
    output_directory_path = Path(output_directory_path)
    output_directory_path.mkdir(parents=True, exist_ok=True)  # Ensure the output directory exists

    # Determine the output filename based on the input directory name
    output_filename = input_directory_path.name + "_merged.csv"

    # Iterate over CSV files in the specified directory matching the pattern
    for file_path in input_directory_path.glob("*_*.csv"):
        # Extract year from the filename using regex
        match = re.search(pattern, file_path.name)
        if match:
            year = match.group(1)
            # Read the CSV file, skipping the header row
            data = pd.read_csv(file_path, header=None, names=['Key', 'Value'], skiprows=1)

            # Process each key-value pair in the current CSV
            for index, row in data.iterrows():
                key = row['Key']
                value = row['Value']

                # If it's the first file, add a Year column and initialize keys as columns
                if 'Year' not in merged_data.columns:
                    merged_data['Year'] = [year]
                    for key in data['Key']:
                        merged_data[key] = None  # Initialize new columns for keys

                # Check if the year is already in the dataframe, if not, add a new row for it
                if year not in merged_data['Year'].values:
                    new_row = {'Year': year}
                    merged_data = pd.concat([merged_data, pd.DataFrame([new_row])], ignore_index=True)

                # Update the value in the dataframe
                merged_data.loc[merged_data['Year'] == year, key] = value

    # Reorder the merged data by Year
    merged_data = merged_data.sort_values('Year').reset_index(drop=True)

    # Save the merged DataFrame to a new CSV file in the output directory
    merged_output_path = output_directory_path / output_filename
    merged_data.to_csv(merged_output_path, index=False)

    print(f"Merged data saved to {merged_output_path}")

# Directories to process
directories = ["new_applicants", "old_applicants"]
base_directory_path = "data/cleaned"
output_directory_path = "data/merged"

# Process each directory
for directory in directories:
    input_directory_path = f"{base_directory_path}/{directory}"
    merge_csv_files(input_directory_path, output_directory_path)
