from skimage.measure import compare_ssim
import cv2
import os

try:
  vid = input('Enter the name of the video. Make sure it is in the same directory as this file: ')

  vidcap = cv2.VideoCapture(vid)
  success, image = vidcap.read()
  count = 0
  success = True

  while success:
    success,image = vidcap.read()
    print('Read a new frame: ' + str(success) + ' : ' + str(count))
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    count += 1

    if (count > 1):
        imageA = cv2.imread("frame" + str(count - 2) +".jpg" , 0)
        imageB = cv2.imread("frame"+str(count - 1)+".jpg" , 0)
        
        score = compare_ssim(imageA, imageB)
        
        if (score > 0.987):
            os.remove("frame%d.jpg" % (count - 2))

except Exception as e:
  print(e)
  input('Press ENTER to exit: ')

          

