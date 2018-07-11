from pandas import Series
class HYUN_Series:
    def Series_Fromat(self):
        house_price = Series([10, 20, 30, 40, 50])
        print(house_price)
    def Series_Fromat_Index(self):
        house_price = Series([10, 20, 30, 40, 50],
                             index=['강원','인천','전라','제주','서울'])
        print(house_price)
        print(house_price['제주'])
        print(house_price.index)
        print(house_price.values)
        print(house_price-5)
        #indexing
        print(house_price[[0,3]])
        #slicing
        print(house_price[0:3])
Hyun=HYUN_Series
Hyun.Series_Fromat(0)
Hyun.Series_Fromat_Index(0)