from bs4 import BeautifulSoup
import pandas as pd

######
# INPUT YOUR VARIABLES HERE
######
your_file_name = "genesets.v2023.1.Hs"
excel_columns = ["STANDARD_NAME", "SYSTEMATIC_NAME", "DESCRIPTION_BRIEF"]
excel_file_name = "test" # This is optional. Will just have same name as input file if not changed
######
# INPUT YOUR VARIABLES HERE
######

# result variables
excel_index = []
excel_formatted_data = []

# Opening the file
with open("./" + your_file_name + ".xml", 'r') as f:
    data = f.read()
 
# parsing data to python
raw_data = BeautifulSoup(data, "xml")
 
# getting into all the rows of data
rows_of_data = raw_data.find('MSIGDB', {'NAME':'search results'})

# Going through each row of data getting the specific columns you need
for row in rows_of_data.find_all('GENESET'):
    excel_index.append(row["STANDARD_NAME"])

    column_data = []

    for column_name in excel_columns:
        column_data.append(row[column_name])

    excel_formatted_data.append(column_data)

# exporting_to_excel
data_frame = pd.DataFrame(excel_formatted_data,
                  index=None, columns=excel_columns)
if len(excel_file_name) == 0:
    data_frame.to_excel(your_file_name + '.xlsx', sheet_name=your_file_name)
else:
    data_frame.to_excel(excel_file_name + '.xlsx', sheet_name=your_file_name)
