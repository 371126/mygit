class Compare:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符是否在别一个字符中
        str_one : 期望结果中的数据
        str_two : 返回的数据
        '''
        res = None
        if str_one in str_two:
            res = True
        else:
            res = False

        return res