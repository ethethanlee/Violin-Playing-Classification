import cv2
import numpy as np
# import keyboard


cap = cv2.VideoCapture('200x200_data/videos/corelli_unsure.mp4') #allPizz_almost.mp4
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# vidObj = cv2.VideoCapture('nahhh.mp4')
frame = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

fc = 0
ret = True

# while (fc < frameCount  and ret):
#     ret, frame[fc] = cap.read()
#     fc += 1

# print(frameCount)

# cap.release()
success = 1
# i = -1
i = 0
while success:
    i = i + 1
    # value = input("Please enter a string:\n")
 
    # print(f'You entered {value}')
    success, frame = cap.read()
    cv2.namedWindow('frame ' + str(i+1))
    # print('hello')
    cv2.imshow('frame ' + str(i+1), frame)
    # cv2.waitKey(0)
    # if value=='q':
    #     #print(0xff)
    #     folder = 'not_playing'
    # if value=='w':
    #     #print(0xff)
    #     folder = 'bow_playing'
    # if value=='e':
    #     folder = 'pizz'
    # folder = 'bow_playing'
    # folder = 'not_playing'
    # folder = 'pizz'
    folder = 'unsure'
    # Save Frame by Frame into disk using imwrite method
    if i%235 == 0:
        cv2.imwrite('200x200_data/3_classes_data/validation/'+ folder + '/test_corelli_' + folder + '_'+str(i)+'.jpg', frame)
        print('frame done for sure')
    elif i%47 == 0:
        cv2.imwrite('200x200_data/3_classes_data/train/'+ folder + '/test_corelli_' + folder + '_'+str(i)+'.jpg', frame)
        print('frame done')