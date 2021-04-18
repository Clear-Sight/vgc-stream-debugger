import cv2
import zmq
import base64
import numpy as np

context = zmq.Context.instance()
dish = context.socket(zmq.DISH)
dish.rcvtimeo = 1000
dish.bind('udp://*:7777')
dish.join('feed')
dish.setsockopt_string(zmq.DISH, np.unicode(''))

while True:
    try:
        image_string = dish.recv_string()
        raw_image = base64.b64decode(image_string)
        image = np.frombuffer(raw_image, dtype=np.uint8)
        frame = cv2.imdecode(image, 1)
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break

dish.close()
context
.term()
