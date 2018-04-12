from request_url.request_method import Request_method
from data.get_data import Get_Data
from operation_tool.compare import Compare
import json
class RunTest():
    def __init__(self):
        self.run_method = Request_method()
        self.getData = Get_Data()
        self.compare = Compare()
    #执行程序
    def run_test(self,filename):
        case_count = self.getData.get_excel_lines()
        for i in range(1,case_count):
            url = self.getData.get_request_url(i)
            method = self.getData.get_method(i)
            data = self.getData.get_data_for_json(filename)
            header = json.loads(self.getData.get_header(i))
            is_run = self.getData.if_is_run(i)
            exp_restult = self.getData.get_exp_result(i)
            if is_run == True:
                res = self.run_method.run_requests(method,url,data,header)
                if self.compare.is_contain(exp_restult,res):
                    #print("测试通过")
                    self.getData.write_exl_result(i,u"测试通过")
                else:
                    #print("测试失败")
                    self.getData.write_exl_result(i,u"测试失败")
            return res

if __name__ == "__main__":
    a = RunTest()
    restuls = a.run_test("/Users/yinyu/work/project/mytestcase/login.json")
    #print((restuls.text).encode("utf-8").decode("unicode-escape"))
    print(restuls)
    #print(restuls.s)
    #print(type(restuls.text))