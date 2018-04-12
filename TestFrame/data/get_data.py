from operation_tool.operation_excel import  OperationExcel
import data.data_config
from operation_tool.operation_json import Operation_json
class Get_Data:
    def __init__(self):
        self.operation_excel = OperationExcel()
    #获取excel行数
    def get_excel_lines(self):
        lines = self.operation_excel.get_sheet_lines()
        return lines
    #是否运行
    def if_is_run(self,row):
        res = None
        col = int(data.data_config.get_is_run())
        result =  self.operation_excel.get_table_values(row,col)
        if result == "yes":
            res = True
        else:
            res = False
        return res
    #获取请求方式
    def get_method(self,row):
        col = int(data.data_config.get_request_mothod())
        res = self.operation_excel.get_table_values(row,col)
        return res
    #获取url
    def get_request_url(self,row):
        col = int(data.data_config.get_url())
        url = self.operation_excel.get_table_values(row,col)
        return url

    #获取header
    def get_header(self,row):
        col = int(data.data_config.get_header())
        header = self.operation_excel.get_table_values(row,col)
        return header
    #获取请求数据
    def get_data(self,row):
        col = int(data.data_config.get_request_data())
        content = self.operation_excel.get_table_values(row,col)
        if content == '':
            return None
        else:
            return content
    def get_data_for_json(self,filename):
        oper_json = Operation_json(filename)
        request_data = oper_json.get_json_data()
        return request_data
    #获取预期结果
    def get_exp_result(self,row):
        col = int(data.data_config.get_expect_result())
        exp_result = self.operation_excel.get_table_values(row,col)
        if exp_result == "":
            return None
        else:
            return exp_result
    def get_actual_result(self,row):
        col = int(data.data_config.get_result())
        #actual_result = self.operation_excel.get_table_values(row,col)
        return col

    def write_exl_result(self,row,value):
        col = int(data.data_config.get_result())
        self.operation_excel.write_data(row,col,value)
