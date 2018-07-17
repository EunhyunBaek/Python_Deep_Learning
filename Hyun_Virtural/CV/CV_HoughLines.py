# -*- coding: cp949 -*-
# -*- coding: utf-8 -*- # 한글 주석쓰려면 이거 해야함
import cv2  # opencv 사용
import numpy as np
from PIL import ImageGrab
lower_white = np.array([200,200,200])
upper_white = np.array([255,255,255])

def grayscale(img):  # 흑백이미지로 변환
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def canny(img, low_threshold, high_threshold):  # Canny 알고리즘
    return cv2.Canny(img, low_threshold, high_threshold)


def gaussian_blur(img, kernel_size):  # 가우시안 필터
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices, color3=(255, 255, 255), color1=255):  # ROI 셋팅

    mask = np.zeros_like(img)  # mask = img와 같은 크기의 빈 이미지

    if len(img.shape) > 2:  # Color 이미지(3채널)라면 :
        color = color3
    else:  # 흑백 이미지(1채널)라면 :
        color = color1

    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움
    cv2.fillPoly(mask, vertices, color)

    # 이미지와 color로 채워진 ROI를 합침
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image


def draw_lines(img, lines, color=[0, 0, 255], thickness=2):  # 선 그리기
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)
            print("시작좌표:(",x1,",",y1,")","끝좌표:","(",x2,",",y2,")")



def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):  # 허프 변환
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)

    return line_img


def weighted_img(img, initial_img, α=1, β=1., λ=0.):  # 두 이미지 operlap 하기
    return cv2.addWeighted(initial_img, α, img, β, λ)

while(True):
    image = ImageGrab.grab(bbox=(60, 40, 800, 630))
    printScreen = np.array(image)
    #image = cv2.imread('Line.jpg')  # 이미지 읽기
    #height, width = image.shape[:2]  # 이미지 높이, 너비
    width=800
    height=630
    #print(width, height)

    gray_img = grayscale(printScreen)  # 흑백이미지로 변환

    blur_img = gaussian_blur(gray_img, 3)  # Blur 효과

    canny_img = canny(blur_img, 70, 210)  # Canny edge 알고리즘
    inrange_img = cv2.inRange(printScreen, lower_white, upper_white)
    vertices = np.array(
        [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60), (width - 50, height)]],
        dtype=np.int32)
    # ROI_img = region_of_interest(canny_img, vertices)  # ROI 설정
    ROI_img = region_of_interest(inrange_img, vertices)  # ROI 설정
    cv2.imshow('result1', canny_img)
    cv2.imshow('result2', ROI_img)

    # hough_img = hough_lines(ROI_img, 1,np.pi / 180, 30, 10, 20)  # 허프 변환
    # hough_img = hough_lines(canny_img, 1,np.pi / 180, 30, 10, 20)  # 허프 변환
    hough_img = hough_lines(inrange_img, 1, np.pi / 180, 1, 1, 1)  # 허프 변환

    result = weighted_img(hough_img, printScreen)  # 원본 이미지에 검출된 선 overlap
    #result = weighted_img(printScreen, hough_img)  # 원본 이미지에 검출된 선 overlap

    cv2.imshow('lineresult', printScreen)  # 결과 이미지 출력
    cv2.imshow('lineresult2', hough_img)  # 결과 이미지 출력
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
