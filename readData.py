import os
import xlrd

# read from resources folder
package_dir = os.path.dirname(os.path.abspath(__file__))
firstFile = os.path.join(package_dir+'/resources', 'sample.xlsx')
secondFile = os.path.join(package_dir+'/resources', 'sample1.xls')

# first file
workbook = xlrd.open_workbook(firstFile, "rb")
sheet = workbook.sheet_by_index(0)

# second file
workbook1 = xlrd.open_workbook(secondFile, "rb")
sheet1 = workbook1.sheet_by_index(0)

# print("Total no of columns: ", sheet.nrows)
# print("Total no of rows: ", sheet.ncols)

# find row index
def find_row_index(searchValue):
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i, 0) == searchValue:
            row_index = i
            break
    return row_index


for i in range(1, sheet.nrows):
    name = sheet.cell_value(i, 0)
    age = sheet.cell_value(i, 4)

    row_index_from_second = find_row_index(name)
    age1 = sheet1.cell_value(row_index_from_second, 4)

    if age == age1:
        print("True")
    else:
        print("False")
