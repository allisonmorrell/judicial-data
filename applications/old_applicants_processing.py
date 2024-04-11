
import os
import pandas as pd
from bs4 import BeautifulSoup

# Directory paths
raw_dir = 'data/raw/old_applicants'
processed_dir = 'data/processed/old_applicants'

print('Processing old applicants...')
for filename in os.listdir(raw_dir):
    if filename.endswith('.html'):
        year = filename.split('_')[2]
        html_path = os.path.join(raw_dir, filename)
        csv_path = os.path.join(processed_dir, f'old_applicants_{year}.csv')
        print(f'Processing file: {filename} for year: {year}')

        # Read and parse the HTML file
        with open(html_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            table = soup.find('table')
        print(f'HTML file read and parsed for {filename}')

        # Convert the first table to CSV
        df = pd.read_html(str(table))[0]
        df.to_csv(csv_path, index=False)
        print(f'CSV file created at {csv_path}')