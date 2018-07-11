from pandas import DataFrame, Series

class Hyun_Control:
    #none는 카운트에 포함되지 않음
    data = {
            '연도'    :   [2010, 2011, 2012, 2011, 2012],
            '가격'    :   [10, 15, 20, None, 5]
           }
    data2 = {
            '연도'    :   [2010, 2011, 2012, 2011, 2012],
            '가격'    :   [10, 15, 20, 30, 5]
           }
    s   =   Series([1, 2, 3, None, 5])
    s1  =   DataFrame(data)
    s2  =   DataFrame(data2)
    s3  =   s1.T
    def DataFrame_Sum(self):
        print(Hyun_Control.DataFrame_Sum)
        print(Hyun_Control.s2)
        print('Sum  :   \n',Hyun_Control.s2.sum())
        print(Hyun_Control.s3)
        print(Hyun_Control.s3.sum(axis=1))
    def Print(self):
        print(Hyun_Control.Print)
        print('Series Count',Hyun_Control.s.count())
        print(Hyun_Control.s1)
        print(Hyun_Control.s1.count())
        Hyun_Control.DataFrame_Sum(0)

hyun = Hyun_Control
hyun.Print(0)