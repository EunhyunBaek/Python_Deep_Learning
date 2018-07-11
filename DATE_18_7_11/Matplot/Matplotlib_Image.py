import matplotlib.pyplot as plt
from matplotlib.image import imread
class Hyun_Image:
    img=imread('test.jpg')
    def Show_Image(tself):
        plt.imshow(Hyun_Image.img)
        plt.show()
hyun = Hyun_Image
hyun.Show_Image(0)