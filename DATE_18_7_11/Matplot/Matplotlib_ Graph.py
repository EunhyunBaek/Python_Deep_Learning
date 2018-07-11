import matplotlib.pyplot as plt

class Hyun_Graph:
    #if dont have xlie ,x value have a y index number
    input_value     =   [1, 4, 9, 16, 25]
    x_input_value   =   [1, 2 ,3 ,4 ,5 , 6]
    y_input_value   =   [1, 4, 9, 16, 25, 36]
    def Draw_In_ValueY_One_Dimensional_Graph(self):
        plt.plot(Hyun_Graph.input_value)
        plt.show()
    def Draw_In_ValueXY_One_Dimensional_Graph(self):
        plt.plot(Hyun_Graph.x_input_value,Hyun_Graph.y_input_value)
        plt.show()
    def EditDraw_One_Dimensional_Graph(self):
        plt.plot(Hyun_Graph.x_input_value,Hyun_Graph.y_input_value,linewidth=5)
        plt.title("Get Square",fontsize=20)
        plt.xlabel("X Value",fontsize=20)
        plt.ylabel("Y Value",fontsize=20)
        plt.tick_params(axis='both',labelsize=15)
        plt.show()
    def DrawScatter_One_Dimensional_Graph(self):
        plt.scatter(Hyun_Graph.x_input_value,Hyun_Graph.y_input_value,s=20)
        plt.show()
hyun=Hyun_Graph
hyun.Draw_In_ValueY_One_Dimensional_Graph(0)
hyun.Draw_In_ValueXY_One_Dimensional_Graph(0)
hyun.EditDraw_One_Dimensional_Graph(0)
hyun.DrawScatter_One_Dimensional_Graph(0)