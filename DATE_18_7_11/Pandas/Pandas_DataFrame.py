from pandas import DataFrame, Series
class Hyun_DataFrame:
    #{}=dir 형태
    data = {
                '지역': ['서울', '서울', '서울', '인천', '인천'],
                '연도': [2010, 2011, 2012, 2011, 2012],
                '가격': [10, 15, 20, 3, 5]
           }
    df  =   DataFrame(data)
    df1 =   DataFrame(data,columns=['지역','연도','가격'],index=['첫째','둘째','셋째','넷째','다섯째'])
    df2 =   DataFrame(data,columns=['지역','연도','가격','인구'],index=['첫째','둘째','셋째','넷째','다섯째'])
    def DataFrame_In_Series(self):
        val=Series([500,500],index=['첫째','넷째'])
        Hyun_DataFrame.df2.인구=val
        print(Hyun_DataFrame.df2)
    def Print(df):
        print(hyun.data)
        print(hyun.df)
        print('df1  :\n',   df)
        print('df1 columns  :\n', df)
        print('df1 index  :\n', df)
        print('df1 index 연도  :\n', df)
        print('df1 index 연도  :\n', df['연도'])
        print('리스트 인덱싱  :\n', df[["연도", "지역"]])
    def DataFrame_Del(self):
        del Hyun_DataFrame.df2['인구']
        #delete
        print(Hyun_DataFrame.df2)
        #{3,2}->{2,3}
        print(Hyun_DataFrame.df2.T)

hyun=Hyun_DataFrame

print(Hyun_DataFrame.Print)
hyun.Print(hyun.df1)
hyun.Print(hyun.df2)
hyun.DataFrame_In_Series(0)
print(Hyun_DataFrame.DataFrame_In_Series)
hyun.df2.인구=100
hyun.Print(hyun.df2)
print(Hyun_DataFrame.DataFrame_Del)
hyun.DataFrame_Del(0)