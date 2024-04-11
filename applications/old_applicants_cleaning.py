# first and last items are applications outstanding as of beginning and end of year - modified the column headers to match
# note special case for 2016, "Applications outstanding as of October 31, 2016 under new assessment process established on October 20, 2016."
# year end for all is end of october (approximately)
# in old data, did highly recommended in first 2005 and 2006 but switched back to just recommended


import os
import pandas as pd

def clean_applicant_data():
    processed_dir = 'data/processed/old_applicants'
    cleaned_dir = 'data/cleaned/old_applicants'
    if not os.path.exists(cleaned_dir):
        os.makedirs(cleaned_dir)

    all_filenames = []
    for filename in os.listdir(processed_dir):
        if filename.endswith('.csv'):
            print(f'Processing file: {filename}')
            df = pd.read_csv(f'{processed_dir}/{filename}')
            df.iloc[0, 0] = 'Applications outstanding at beginning of year'
            df.iloc[-2, 0] = 'Applications outstanding at end of year'
            # Replace double quotations with apostrophes within values of first column
            # Replace left and right quotations with apostrophes
            # Also handle single quotations
            df.iloc[:, 0] = df.iloc[:, 0].str.replace('"', "'").str.replace("‘", "'").str.replace("’", "'")
            df.to_csv(f'{cleaned_dir}/{filename}', index=False)
            all_filenames.append(f'{cleaned_dir}/{filename}')
            print(f'Finished processing file: {filename}')


from pprint import pprint

def get_row_names():
    # for each csv file in 
    cleaned_dir = 'data/cleaned/old_applicants'

    row_names = []

    for filename in os.listdir(cleaned_dir):
        if filename.endswith('.csv'):
            print(f'Processing file: {filename}')
            df = pd.read_csv(f'{cleaned_dir}/{filename}')

            for index, row in df.iterrows():
                if row[0] not in row_names:
                    row_names.append(row[0])

        pprint(row_names)


clean_applicant_data()
get_row_names()