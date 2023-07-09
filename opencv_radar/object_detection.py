import cv2
import time
from collections import namedtuple

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

xy = namedtuple('vertex', ['x', 'y'])
left_up_corner = xy(940, 580)
right_up_corner = xy(left_up_corner.x + 500, left_up_corner.y)
left_down_corner = xy(left_up_corner.x - 800, right_up_corner.y + 1050)
right_down_corner = xy(left_down_corner.x + 1200, left_down_corner.y)

def cli():

    # inputs
    capture = cv2.VideoCapture('traffic.webm')
    vehicles_cascade = cv2.CascadeClassifier('vehicles.xml')

    # distance between horizontal lines in meters
    distance = 12

    # main loop
    frame_count = 0
    while True:
        print("Frame: ", frame_count)
        _, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = vehicles_cascade.detectMultiScale(gray, 1.1, 2)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), blue, 2)

        cv2.line(frame, left_up_corner, right_up_corner, red, 5)      # first horizontal line
        cv2.line(frame, left_down_corner, right_down_corner, red, 5)  # second horizontal line
        cv2.line(frame, left_up_corner, left_down_corner, red, 5)     # first vertical line
        cv2.line(frame, right_up_corner, right_down_corner, red, 5)   # second vertical line

        for(x, y, w, h) in cars:
            time_start = None
            if(left_up_corner.x <= x <= right_up_corner.x and y >= left_up_corner.y):
                time_start = time.time() 
                print("Car Entered.")

            if (left_down_corner.x <= x <= right_down_corner.x and y >= left_down_corner.y):
                time_end = time.time()
                print("Car Left.")

                # we know that distance is 12m
                if time_start:
                    print("Speed in (m/s) is:", distance / ((time_end-time_start)))
            time_start = None

        resized = cv2.resize(frame, (1280, 1024))
        cv2.imshow('img', resized) 

        if cv2.waitKey(27) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()