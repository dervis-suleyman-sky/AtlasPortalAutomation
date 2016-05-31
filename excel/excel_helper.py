'''
Created on 31 May 2016

@author: Dev2
'''

from openpyxl import load_workbook
import warnings

class ExcelHelper(object):


    def __init__(self):
        pass
    
'''
Test Spread sheet reading code


What I want to do is open the excel spread sheet check there is a value in Operation if not, stop the code

read row=3
read col=range[A:BJ]

when test is complete:
    
    ##create an asset via the portal## mark as pass or fail and move onto the next row. break if row contains no operation

read next row

'''
if __name__ == '__main__':
    with warnings.catch_warnings():
        '''Ignore the warning for using .xlsm this is due to the python code expecting a 2006 extension'''
        warnings.simplefilter("ignore")
        '''--------------------------------------------------------------------------------------------'''
        wb = load_workbook(filename='C:\\workspace\\AtlasPortalAutomation\\excel\\excel_documents\\NBCU_Syfy_Metadata Schedule_160524_RN.xlsm')
        print("-----------------------------------------")
        print("Active work sheet=["+str(wb.active)+"]")
        #read the Metadata work sheet
        sheet=wb.get_sheet_by_name('Metadata spreadsheet')
        #check the title of the work sheet can be found
        print(sheet.title)
        print("-----------------------------------------")
        
        '''iterate over each row'''
        for row_number in range(4, 8):
            for col_number in range(1,63):
                cell_value=(sheet.cell(row=row_number, column=col_number).value)
                if not cell_value==None:
                    print cell_value

        
        #print sheet['A4'].value,sheet['B4'].value,sheet['C4'].value,sheet['AA4'].value
    