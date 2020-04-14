import pandas as pd 
import xlsxwriter
 



input_df= pd.read_excel(r'C:\Users\DELL\Python stuffs\upwork1\input.xlsx')
output_df= pd.read_excel(r'C:\Users\DELL\Python stuffs\upwork1\output.xlsx')

new_input = xlsxwriter.Workbook(r'C:\Users\DELL\Python stuffs\upwork1\new_input.xlsx')
worksheet = new_input.add_worksheet()
new_columns=[]
#Replace row 1, coloumn 3 of input to mech
for colz in output_df.columns:
    new_columns.append(colz)
print(len(new_columns))

worksheet.write('A1', new_columns[0]) 
worksheet.write('B1', new_columns[1]) 
worksheet.write('C1', new_columns[2]) 
worksheet.write('D1', new_columns[3])
worksheet.write('E1', new_columns[4])
worksheet.write('F1', new_columns[5])
worksheet.write('G1', new_columns[6])
worksheet.write('H1', new_columns[7])
worksheet.write('I1', new_columns[8])
worksheet.write('J1', new_columns[9])
worksheet.write('K1', new_columns[10])
worksheet.write('L1', new_columns[11])

def column_locator(row,column):
    dumping_list=[]
    for j in input_df.iloc[:,column]:
        dumping_list.append(str(j))
    for i in dumping_list : 
        worksheet.write(row, column, i) 
        row += 1

column_locator(1,0)
column_locator(1,1)
column_locator(1,3)
column_locator(1,4)
column_locator(1,5)
column_locator(1,6)
column_locator(1,7)
column_locator(1,8)
column_locator(1,9)
column_locator(1,10)

format = new_input.add_format({'text_wrap': True})


# Setting the format but not setting the column width.
worksheet.set_column('A:L', 18, format)


new_input.close()

