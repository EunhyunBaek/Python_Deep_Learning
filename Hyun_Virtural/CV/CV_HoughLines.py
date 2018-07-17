# -*- coding: cp949 -*-
# -*- coding: utf-8 -*- # �ѱ� �ּ������� �̰� �ؾ���
import cv2  # opencv ���
import numpy as np
from PIL import ImageGrab
lower_white = np.array([200,200,200])
upper_white = np.array([255,255,255])

def grayscale(img):  # ����̹����� ��ȯ
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def canny(img, low_threshold, high_threshold):  # Canny �˰���
    return cv2.Canny(img, low_threshold, high_threshold)


def gaussian_blur(img, kernel_size):  # ����þ� ����
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices, color3=(255, 255, 255), color1=255):  # ROI ����

    mask = np.zeros_like(img)  # mask = img�� ���� ũ���� �� �̹���

    if len(img.shape) > 2:  # Color �̹���(3ä��)��� :
        color = color3
    else:  # ��� �̹���(1ä��)��� :
        color = color1

    # vertices�� ���� ����� �̷��� �ٰ����κ�(ROI �����κ�)�� color�� ä��
    cv2.fillPoly(mask, vertices, color)

    # �̹����� color�� ä���� ROI�� ��ħ
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image


def draw_lines(img, lines, color=[0, 0, 255], thickness=2):  # �� �׸���
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)
            print("������ǥ:(",x1,",",y1,")","����ǥ:","(",x2,",",y2,")")



def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):  # ���� ��ȯ
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)

    return line_img


def weighted_img(img, initial_img, ��=1, ��=1., ��=0.):  # �� �̹��� operlap �ϱ�
    return cv2.addWeighted(initial_img, ��, img, ��, ��)

while(True):
    image = ImageGrab.grab(bbox=(60, 40, 800, 630))
    printScreen = np.array(image)
    #image = cv2.imread('Line.jpg')  # �̹��� �б�
    #height, width = image.shape[:2]  # �̹��� ����, �ʺ�
    width=800
    height=630
    #print(width, height)

    gray_img = grayscale(printScreen)  # ����̹����� ��ȯ

    blur_img = gaussian_blur(gray_img, 3)  # Blur ȿ��

    canny_img = canny(blur_img, 70, 210)  # Canny edge �˰���
    inrange_img = cv2.inRange(printScreen, lower_white, upper_white)
    vertices = np.array(
        [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60), (width - 50, height)]],
        dtype=np.int32)
    # ROI_img = region_of_interest(canny_img, vertices)  # ROI ����
    ROI_img = region_of_interest(inrange_img, vertices)  # ROI ����
    cv2.imshow('result1', canny_img)
    cv2.imshow('result2', ROI_img)

    # hough_img = hough_lines(ROI_img, 1,np.pi / 180, 30, 10, 20)  # ���� ��ȯ
    # hough_img = hough_lines(canny_img, 1,np.pi / 180, 30, 10, 20)  # ���� ��ȯ
    hough_img = hough_lines(inrange_img, 1, np.pi / 180, 1, 1, 1)  # ���� ��ȯ

    result = weighted_img(hough_img, printScreen)  # ���� �̹����� ����� �� overlap
    #result = weighted_img(printScreen, hough_img)  # ���� �̹����� ����� �� overlap

    cv2.imshow('lineresult', printScreen)  # ��� �̹��� ���
    cv2.imshow('lineresult2', hough_img)  # ��� �̹��� ���
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
