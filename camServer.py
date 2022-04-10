import cv2
import time
import picamera
from picamera.array import PiRGBArray
import os
from flask import Flask,jsonify,render_template,make_response,request, Response, send_from_directory

#init
app = Flask(__name__,template_folder='template')
camera = picamera.PiCamera()
alert_update_interval = 10 # alert only once in this time interval
object_classifier = cv2.CascadeClassifier("models/upperbody_recognition_model.xml") # an opencv classifier
last_epoch = 0
log_list = [];

try:
    camera.vflip = True
    camera.hflip = True
    camera.resolution = (640, 480)
    rawCapture = PiRGBArray(camera, size=(640, 480))
    # Start a preview and let the camera warm up for 2 seconds
    time.sleep(0.1)
    camera.start_preview()
finally:
    camera.stop_preview()

def get_object(frame, classifier):
    found_objects = False
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = classifier.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if len(objects) > 0:
        found_objects = True
    # Draw a rectangle around the objects
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    ret, jpeg = cv2.imencode('.jpg', frame)
    return (jpeg.tobytes(), found_objects)

def gen2():
    while True:
        camera.capture("image.jpg")
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + open('image.jpg', 'rb').read() + b'\r\n')
    
#capture image from camera
def gen():
    global last_epoch, log_list
    while True:
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        flame, found_obj = get_object(image, object_classifier)
        rawCapture.truncate(0)
        if found_obj and (time.time() - last_epoch) > alert_update_interval:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            log_list.append(current_time + " - [Warning] Smart security cam found object")
            last_epoch = time.time()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + flame + b'\r\n')

@app.route("/")
def renderMainPage():
    try:
        return render_template("info.html")
    except Exception as error:
        print(error)
        response = make_response(jsonify({"error":"Page not found"}),404)
    return response

@app.route('/stream_video')
def stream_video():
    return Response(gen2(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/startRecord')
def start_record():
    try:
        filename = 'video'+ str(time.time()) + '.h264'
        camera.start_recording(filename)
        response = make_response(jsonify({"status":"success", "filename":filename}),200)
    except Exception as error:
        print(error)
        response = make_response(jsonify({"status":"failed"}),200)
    return response
    
@app.route('/stopRecord')
def stop_record():
    try:
        camera.stop_recording()
        response = make_response(jsonify({"status":"success"}),200)
    except Exception as error:
        response = make_response(jsonify({"status":"failed"}),200)
    return response
    
@app.route('/downRecord', methods=['GET', 'POST'])
def downRecord():
    args = request.args
    filename = args.get("filename")
    print(filename)
    return send_from_directory(directory=os.getcwd(), filename=filename,as_attachment=True)

@app.route('/getLog', methods=['GET'])
def get_msg():
    result = {
        'text': log_list,
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
