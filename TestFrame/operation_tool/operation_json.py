import json
class Operation_json:
    def __init__(self,filename):
        self.filename = filename
        self.data = self.get_json_data()

    def get_json_data(self):
        with open(self.filename) as jf:
            self.data = json.load(jf)
            return self.data

    def get_json_value(self,key=None):
        return self.data[key]

if __name__ == "__main__":
    filename = "/Users/yinyu/work/project/mytestcase/login.json"
    j = Operation_json(filename)
    print(j.get_json_value())
