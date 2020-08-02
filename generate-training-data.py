import os
import cv2

# write your code here to open your laptop's camera
# and store images for rock paper scissors

# I would highly recommend storing these images in folders stucture like below:
# training_data\
#           |-- empty\
#           |-- rock\
#           |-- paper\
#           |-- scissors\
# having a folder structure like this will make it easy for you to read the images while pre-processing


cap = cv2.VideoCapture(0)


#def FolderCreation(x):
count = 0
#root = 'D:/Downloads/rock-paper-scissors-master/rock-paper-scissors-master'
#folder = str(input('1.empty\n2.rock\n3.paper\n4.scissor\n'))

while(True):
    rep, frame = cap.read()

    frame = cv2.rectangle(frame, (40, 40), (350, 350), (255, 255, 255), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame,"Press space when ready",(35,400),font,1,(255,255,255),2)

    cv2.imshow('Images',frame)
    start_row,start_col = int(45),int(75)
    end_row,end_col = int(320),int(335)
    frame = frame[start_row:end_row,start_col:end_col]

    k = cv2.waitKey(1)
    if k%256 == 27:  #escape
        break
    elif k%256 == 32: #space
        name = "frame_{}.png".format(count)
        #cv2.imwrite('D:/Downloads/rock-paper-scissors-master/rock-paper-scissors-master/'+folder+'/image'+str(count)+'.png',frame)
        cv2.imwrite(name,frame)
        print("{} image written!".format(count))
        count += 1


cap.release()
cv2.destroyAllWindows()

#shape = input('Rock? Paper? Scissor?')
#FolderCreation(shape)