import ffmpeg
#from  transformers import transformer_start
def frame_start(filepath):
  #folder='/content/gdrive/MyDrive/Capstone'
  print("Check point 1")
  folder='/mnt/c/Users/Hp/Desktop/'
  openpose_video="/mnt/c/Users/Hp/Desktop/Red_0.avi"
  print("Check point 2")
  probe = ffmpeg.probe(openpose_video)
  print("Check point 3")
  time = float(probe['streams'][0]['duration'])
  width = probe['streams'][0]['width']
  parts = 16
  print("Check point 4")
  intervals = time /parts
  interval_list = [(j * intervals, (j + 1) * intervals) for j in range(parts)]
  print("Check point 5")

  j=0
  for item in interval_list:
    (
      ffmpeg
      .input(openpose_video, ss=item[1])
      .filter('scale', width, -1)
      .output(folder+'/'+'Frames'+'/'+'Red'+'_'+str(j)+'.jpg', vframes=1)
      .run()
    )
    print("Check point 6")
    j+= 1
    print("Check point 7")
    #transformer_start()
  
frame_start("FO")
    
