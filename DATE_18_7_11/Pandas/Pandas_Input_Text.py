import pandas as pd
class Hyun_Input_Text:
    #\s is spacebar sep = seperlater? (구분자 스페이스)
    iris2 = pd.read_table(
        'iris2.txt', sep='\s+',
        names=['s1', 'sw', 'pl', 'pw', 'regression']
    )
    iris3 = pd.read_table(
        'iris2.txt', sep='\s+',
        names=['s1', 'sw', 'pl', 'pw', 'regression'],
        skiprows=[0,1]
    )
    def Write_Text(self):
        Hyun_Input_Text.iris2.to_csv('iris3.csv')
        Hyun_Input_Text.iris3.to_csv('iris4.csv')
    def Print(self):
        print(Hyun_Input_Text.Print)
        print(Hyun_Input_Text.iris2)
        print(Hyun_Input_Text.iris3)

hyun=Hyun_Input_Text
hyun.Print(0)
hyun.Write_Text(0)