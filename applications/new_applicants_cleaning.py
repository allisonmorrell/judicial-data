
# Remove excess tabs white space in last row

# Replace  with "Applications received during the year."

# Map first row data to these new headings: 


import os
import pandas as pd


def clean_applicant_data():
    processed_dir = 'data/processed/new_applicants'
    cleaned_dir = 'data/cleaned/new_applicants'
    if not os.path.exists(cleaned_dir):
        os.makedirs(cleaned_dir)

    for filename in os.listdir(processed_dir):
        if filename.endswith('.csv'):
            print(f'Processing file: {filename}')
            df = pd.read_csv(f'{processed_dir}/{filename}', header=None)

            # Remove placeholder rows based on a specific string pattern
            df = df[~df.iloc[:, 0].str.contains("Unnamed", na=False)]

            # Clean all string cells of excess whitespace (spaces, new lines, tabs)
            df = df.applymap(lambda x: ' '.join(x.split()) if isinstance(x, str) else x)

            # Replace the string "Judges Appointed" with "Newly Appointed Judges"
            df = df.replace('Judges Appointed', 'Newly Appointed Judges')
            
            # Save the cleaned DataFrame
            df.to_csv(f'{cleaned_dir}/{filename}', index=False)
            print(f'Finished processing file: {filename}')

clean_applicant_data()