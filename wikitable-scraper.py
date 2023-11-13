import requests
from bs4 import BeautifulSoup
import csv

# Specifying the source URL
url = 'https://en.wikipedia.org/wiki/Demographics_of_Mauritius'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# Finding all tables with the "wikitable" class 
all_tables = soup.find_all("table", attrs={"class": "wikitable"})

table_number = 1

# Iterating through tables

for table in all_tables:

    table_data = table.find_all("tr")

    final_data = []

    # Iterating through rows in the table
    for tr in table_data:
        t_row = []

        # Iterating through cells in the row
        for td in tr:
            if (td.string != '\n'):
                t_row.append(td.text.rstrip('\n'))

        # Creating an array from the table
        final_data.append(t_row)

    filename = "table_" + str(table_number) + ".csv"
    table_number += 1

    # Writing the array to a .csv file 
    with open(filename, "w+", newline='', encoding="utf-8") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(final_data)

print("Saved {} tables from {}.".format(table_number-1, url))
