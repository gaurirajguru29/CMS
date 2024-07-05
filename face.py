import cv2


#video=cv2.VideoCapture(0)

#while True:
  #  ret, frame=video.read()
 #   if cv2.waitKey(10)== ord('q'):
   #     breaks
  #  cv2.iashow("image" ,frame)

def return_camera_indices():
    index= -2
    arr=[]
    i=10
    while i > 0:
        cap=cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i-=1
    return arr