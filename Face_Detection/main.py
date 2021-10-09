import cv2
  
  
 #load haarcascade 
face_cascade = cv2.CascadeClassifier("Face_Detection\haarcascade_frontalface_default.xml")

  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    #read the video capture object
    ret, frame = vid.read()
    #convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    #draw box around faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows 
cv2.destroyAllWindows()
