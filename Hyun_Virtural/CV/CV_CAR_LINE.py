import numpy as np
from PIL import ImageGrab
import cv2
import time
from numpy import ones, vstack
from numpy.linalg import lstsq
#from directkeys import PressKey, W, A, S, D
from statistics import mean


# 4강 참고
def roi(img, vertices):
    # 이미지 크기 만큼의 값이 0으로 채워진 배열 생성
    mask = np.zeros_like(img)

    # mask에서 관심영역(vertices)에만 값을 255(=0x11111111)로 변환
    cv2.fillPoly(mask, vertices, 255)

    # mask에서 값이 1인 부분의 img만 사용하고 0인 부분은 버림
    masked = cv2.bitwise_and(img, mask)

    return masked


# 차선 그리기, 예외 처리 적용
def draw_lanes(img, lines, color=[0, 255, 255], thickness=3):
    # 에러 발생 시, 기본선을 사용
    try:
        # 차량이 움직이면 화면에서 수평선이 항상 같은 지점에 있지 않게 되므로
        # 차선 마커의 최대 y 값을 찾는다

        ys = []
        for i in lines:
            for ii in i:
                ys += [ii[1], ii[3]]  # 직선의 출발점과 도착점의 y 성분들

        min_y = min(ys)
        max_y = 600

        new_lines = []
        line_dict = {}

        for idx, i in enumerate(lines):
            for xyxy in i:
                # http://stackoverflow.com/questions/21565994/method-to-return-the-equation-of-a-straight-line-given-two-points
                # 두 점의 좌표로 선을 생성
                x_coords = (xyxy[0], xyxy[2])
                y_coords = (xyxy[1], xyxy[3])

                # [ [xyxy[0], xyxy[2]],
                #   [      1,       1] ].T =
                # [ [xyxy[0], 1],
                #   [xyxy[2], 1] ]
                A = vstack([x_coords, ones(len(x_coords))]).T  # 전치 행렬

                m, b = lstsq(A, y_coords)[0]  # y_coords = mA + b의 Least Square(최소제곱해) 반환(feat. 선형대수)

                # y = mx + b 였으므로, x = (y - b) / m
                x1 = (min_y - b) / m
                x2 = (max_y - b) / m

                # 차선 추가
                line_dict[idx] = [m, b, [int(x1), min_y, int(x2), max_y]]
                new_lines.append([int(x1), min_y, int(x2), max_y])

        # ... 여기부터는 제가 영어가 부족해서... 코드 해석 좀 대신 부탁드릴께요!!!
        final_lanes = {}

        for idx in line_dict:
            final_lanes_copy = final_lanes.copy()

            m = line_dict[idx][0]
            b = line_dict[idx][1]
            line = line_dict[idx][2]

            if len(final_lanes) == 0:
                final_lanes[m] = [[m, b, line]]

            else:
                found_copy = False

                for other_ms in final_lanes_copy:

                    if not found_copy:
                        if abs(other_ms * 1.2) > abs(m) > abs(other_ms * 0.8):
                            if abs(final_lanes_copy[other_ms][0][1] * 1.2) > abs(b) > abs(
                                    final_lanes_copy[other_ms][0][1] * 0.8):
                                final_lanes[other_ms].append([m, b, line])
                                found_copy = True
                                break
                        else:
                            final_lanes[m] = [[m, b, line]]

        line_counter = {}

        for lanes in final_lanes:
            line_counter[lanes] = len(final_lanes[lanes])

        top_lanes = sorted(line_counter.items(), key=lambda item: item[1])[::-1][:2]

        lane1_id = top_lanes[0][0]
        lane2_id = top_lanes[1][0]

        # 차선 후보들을 평균 내서, 최종 차선 반환
        def average_lane(lane_data):
            x1s = []
            y1s = []
            x2s = []
            y2s = []
            for data in lane_data:
                x1s.append(data[2][0])
                y1s.append(data[2][1])
                x2s.append(data[2][2])
                y2s.append(data[2][3])

            return int(mean(x1s)), int(mea(y1s)), int(mean(x2s)), int(mean(y2s))

        l1_x1, l1_y1, l1_x2, l1_y2 = average_lane(final_lanes[lane1_id])
        l2_x1, l2_y1, l2_x2, l2_y2 = average_lane(final_lanes[lane2_id])

        return [l1_x1, l1_y1, l1_x2, l1_y2], [l2_x1, l2_y1, l2_x2, l2_y2]

    # 예외처리
    except Exception as e:
        print(str(e))


# BGR to Gray -> Canny Edge Detection -> 가우시안 정규화 -> 관심영역 필터링 -> 허프 직선검출 -> 차선 검출 -> 차선 그리기
def process_img(image):
    original_image = image
    # convert to gray
    #processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    #processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)

    #processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)

    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500],
                         ], np.int32)



    # 5강 참고
    lower_white = np.array([150, 150, 150])
    upper_white = np.array([255, 255, 255])
    inrange_img = cv2.inRange(original_image, lower_white, upper_white)
    cv2.Canny(inrange_img, threshold1=200, threshold2=300)
    processed_img = roi(inrange_img, [vertices])

    #hough_img = hough_lines(inrange_img, 1, np.pi / 180, 1, 1, 1)  # 허프 변환
    #lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 10, 30, 30)
    lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 10, 100, 10)
    try:
        l1, l2 = draw_lanes(inrange_img, lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        print(str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(original_image, (coords[0], coords[1]), (coords[2], coords[3]), [255, 0, 0], 3)


            except Exception as e:
                print(str(e))
    except Exception as e:
        pass

    return inrange_img, original_image


def main():
    last_time = time.time()
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))

        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        new_screen, original_image = process_img(screen)

        cv2.imshow('window', new_screen)
        cv2.imshow('window2', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()