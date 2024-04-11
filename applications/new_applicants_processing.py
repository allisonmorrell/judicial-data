

# Script to just get the totals from the data from the new years (excluding demographic data)

# example file: https://www.fja.gc.ca/appointments-nominations/StatisticsCandidate-StatistiquesCandidat-2023-eng.html


import os
import pandas as pd
from bs4 import BeautifulSoup

# Directory paths
raw_dir = 'data/raw/new_applicants'
processed_dir = 'data/processed/new_applicants'

print('Processing new applicants...')
for filename in os.listdir(raw_dir):
    if filename.endswith('.html'):
        year = filename.split('_')[2]
        html_path = os.path.join(raw_dir, filename)
        csv_path = os.path.join(processed_dir, f'new_applicants_{year}.csv')
        print(f'Processing file: {filename} for year: {year}')

        # Read and parse the HTML file
        with open(html_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            table = soup.find('table')
        print(f'HTML file read and parsed for {filename}')

        # Convert the first table to CSV and save only the first two columns
        df = pd.read_html(str(table))[0].iloc[:, [0, 1]]
        df.to_csv(csv_path, index=False)
        print(f'CSV file created at {csv_path}')


        # Take the first paragraph tag after the first table, create a new row in the CSV, first column "Note", second column put in the text from that paragraph
        note_paragraph = soup.find('table').find_next('p').text
        note_df = pd.DataFrame({'Note': ['Note'], 'Text': [note_paragraph]})
        note_df.to_csv(csv_path, mode='a', header=False, index=False)
        print(f'Note added to CSV file at {csv_path}')