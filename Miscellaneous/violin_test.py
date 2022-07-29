import cv2
import numpy as np

cap = cv2.VideoCapture('allPizz_almost.mp4')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

fc = 0
ret = True

while (fc < frameCount  and ret):
    ret, frame[fc] = cap.read()
    fc += 1

# print(frameCount)
folder = ''
# cap.release()

for i in range (frameCount):
    cv2.namedWindow('frame ' + str(i+1))
    cv2.imshow('frame ' + str(i+1), frame[i])
    cv2.waitKey(0)
    # if cv2.waitKey(0) & 0xff == ord('q'):
    #     folder = 'notPlaying'
    # if cv2.waitKey(0) & 0xff == ord('w'):
    #     folder = 'bowPlaying'
    # if cv2.waitKey(0) & 0xff == ord('e'):
    #     folder = 'colLegno'
    # if cv2.waitKey(0) & 0xff == ord('r'):
    #     folder = 'pizz'
    # Save Frame by Frame into disk using imwrite method
    # writeStatus = cv2.imwrite('/Frame'+str(i)+'.jpg', frame)
    # if writeStatus is True:
    #     print('yay')
    #     print(folder)
    # else:
    #     print('aw')
    #     print(folder)




