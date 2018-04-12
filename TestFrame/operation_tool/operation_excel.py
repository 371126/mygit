import xlrd
from xlutils.copy import copy
class OperationExcel:

    def __init__(self,filename=None,sheet_id=None):
        #如果有传参，就用传进的参数，没有就用默认值
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
        else:
            self.filename = "/Users/yinyu/work/project/mytestcase/mytestcase_Imooc"
            self.sheet_id = 0
        self.data = self.get_excel_data()
    #获取sheet内容
    def get_excel_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取sheet的行数
    def get_sheet_lines(self):
        lines = self.data.nrows
        return lines
    #获取某一单元格的内容
    def get_table_values(self,row,col):
        values = self.data.cell(row,col).value
        return values
    def write_data(self,row,col,value):
        read_data = xlrd.open_workbook(self.filename)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.filename)
if __name__ == "__main__":
    filename = "/Users/yinyu/work/project/mytestcase/mytestcase_Imooc.xlsx"
    ex = OperationExcel(filename,0)

    print(ex.get_sheet_lines())
    print(ex.get_table_values(1,1))