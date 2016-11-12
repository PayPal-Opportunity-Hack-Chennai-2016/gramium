import xlrd
from collections import OrderedDict
import simplejson as json

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('/Users/soundaryat/Desktop/Icici 15th repayment.xlsx')
sh = wb.sheet_by_index(0)

# List to hold dictionaries
cars_list = []

# Iterate through each row in worksheet and fetch values into dict
for rownum in range(2, sh.nrows):
    cars = OrderedDict()
    row_values = sh.row_values(rownum)
    cars['AGREEMENTNO'] = row_values[0]
    cars['CUSTOMERNAME'] = row_values[1]
    cars['EMISTDT'] = row_values[2]
    cars['1st Emi'] = row_values[3]
    cars['EMIENDDT'] = row_values[3]
    cars['DUEDATE'] = row_values[3]
    cars['EMI'] = row_values[3]
    cars['MOBILE'] = row_values[3]
    cars['FINWARE_ACNO'] = row_values[3]
    cars['DMA'] = row_values[3]
    cars['DO Name'] = row_values[3]
    cars['Address'] = row_values[3]
    cars_list.append(cars)

# Serialize the list of dicts to JSON
j = json.dumps(cars_list)

# Write to file
with open('datac.json', 'w') as f:
    f.write(j)