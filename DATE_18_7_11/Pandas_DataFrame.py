from pandas import DataFrame
class Hyun_DataFrame:
    #{}=dir 형태
    data = {
                '지역': ['서울', '서울', '서울', '인천', '인천'],
                '연도': [2010, 2011, 2012, 2011, 2012],
                '가격': [10, 15, 20, 3, 5]
           }
    df  =   DataFrame(data)
    df1 =   DataFrame(data,columns=['지역','연도','가격'],index=['첫째','둘째','셋째','넷째','다섯째'])
    def Print(self):
        print(hyun.data)
        print(hyun.df)
        print('df1  :\n', hyun.df1)
        print('df1 columns  :\n', hyun.df1.columns)
        print('df1 index  :\n', hyun.df1.index)
        print('df1 index 연도  :\n', hyun.df1.연도)
        print('df1 index 연도  :\n', hyun.df1['연도'])
        print('리스트 인덱싱  :\n', hyun.df1[["연도", "지역"]])

hyun=Hyun_DataFrame
hyun.Print(0)