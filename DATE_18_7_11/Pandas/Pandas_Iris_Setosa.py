import pandas as pd

class Hyun_Iris:
    iris = pd.read_csv('iris.csv',
                   names = ['sl', 'sw', 'pl', 'pw', 'regression'])
    def Print(self):
        print(Hyun_Iris.Print)
        print('head  :   ',Hyun_Iris.iris)
        print('head(3)  :   \n',Hyun_Iris.iris.head(3))
        print('head(5)  :   \n', Hyun_Iris.iris.head())#head default is 5

hyun=Hyun_Iris
hyun.Print(0)
