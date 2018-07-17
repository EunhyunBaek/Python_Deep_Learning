import numpy
from PIL import ImageGrab
import cv2

while(True):
    image = ImageGrab.grab(bbox=(60, 40, 800, 630))
    printScreen = numpy.array(image)
    #print('loop took {} seconds'.format(time.time() - last_time))
    #last_time = time.time()
    cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
