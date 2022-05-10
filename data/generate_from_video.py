import cv2
import os
import sys

if(len(sys.argv) == 2):
  path = sys.argv[1]
  filename = path.split("/")[-1].split(".")[0]
  print("Opening", filename)

  os.mkdir(filename)
  vidcap = cv2.VideoCapture(path)
  success,image = vidcap.read()
  count = 0
  while success:
    zer = 8-len(str(count))
    label = zer*'0' + str(count)
    cv2.imwrite(filename+"/%s.png" % label, image)   
    success,image = vidcap.read()
    print('Processing frame', count)
    count += 1

else:
  print("Usage: generate_from_video.py [path_to_video]")