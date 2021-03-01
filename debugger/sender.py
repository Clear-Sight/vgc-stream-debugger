import base64
import cv2
import zmq

context = zmq.Context.instance()
radio = context.socket(zmq.RADIO)
radio.connect('udp://localhost:7777')

camera = cv2.VideoCapture(0)

while True:
    try:
        ret, frame = camera.read()
        frame = cv2.resize(frame, (640, 480))
        encoded, buf = cv2.imencode('.jpg', frame)
        image = base64.b64encode(buf)
        radio.send(image, group='feed')
    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
