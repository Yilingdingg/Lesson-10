import cv2 

car_xml="cars.xml"

model=cv2.CascadeClassifier(car_xml)
video_storing=cv2.VideoCapture("cars+cycle.avi")

while True:
    ret, img=video_storing.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars=model.detectMultiScale(gray, 1.5, 1)
    print(cars)

    for (x,y,w,h) in cars:
        cv2.rectangle(img, (x,y), (x+w,y+h), (250,196,230), 2)

    cv2.imshow("Webcam", img)
    key=cv2.waitKey(10)
    if key==27:
        break 