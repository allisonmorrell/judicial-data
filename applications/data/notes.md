
# Unknowns
Do old data appointed numbers include judges elevated to superior courts? For new data, these are included in the text string in "Note". Concluded that they do not include elevations based on gender table numbers.

# Steps taken

## Scraping
Used URL patterns and known years (from navigating website). Didn't keep scripts.

Also got a page from the old data about gender distributions between judges, haven't done anything with it.

## Extracting data
For old data, got whole table. For new data, got just the totals (didn't take the demographic data from the new tables but it can be done.)


## Cleaning
# New data
Replaced column header "Appointed Judges" with "Newly Appointed Judges", per most recent usage. Substantively the same thing, just that the total number including elevated judges is found in the note in plain text.

# Old data
Made column heading punctuation, etc consistent
first and last items are applications outstanding as of beginning and end of year - modified the column headers to match
note special case for 2016, "Applications outstanding as of October 31, 2016 under new assessment process established on October 20, 2016." is 0 (i.e. they wiped old ones and required new applications to be submitted)
Year end for all is end of october (approximately)
In old data, did highly recommended in first 2005 and 2006 but switched back to just recommended

## Merging

### For each separate set
All column headers matched after steps taken in cleaning

For some reason values for 2006 and 2019 went missing and I added them in manually **(not going to track down rn because laziness)**

### For merging different sources together

Done in google sheets, found in summaries
