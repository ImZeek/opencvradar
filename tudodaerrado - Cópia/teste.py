import cv2
import numpy as np
from object_detection import ObjectDetection

#Iniciar ObjectDetection
od = ObjectDetection()

captura = cv2.VideoCapture('traffic_video_object_detection_tracking.webm')

while True:

    #captura p/frame do video
    _, frame = captura.read()

    
        #detetar objeto on frame
    (tipo_objeto, scores, caixas) = od.detect(frame)
    for caixa in caixas:
            print(caixa)

    cv2.imshow("frame", frame)
    #função que mantem o video aberto
    key = cv2.waitKey(1)

    if key == 27:
        break

captura.release()
cv2.destroyAllWindows()