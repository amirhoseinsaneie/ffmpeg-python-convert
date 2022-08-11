from posixpath import dirname
import subprocess
import os
import shutil
from xml.etree.ElementInclude import include
src = './src'
dst = './mp4'

for root, dirs, filenames in os.walk(src, topdown=False):
    #print(filenames)
    if os.path.basename(root) == 'converted' :
        print('converted folder skiped');
        continue;
    for filename in filenames:
        
        print('[INFO] 1',filename)
        try:
            _format = ''
            if ".flv" in filename.lower():
                _format=".flv"
            if ".mp4" in filename.lower():
                _format=".mp4"
            if ".avi" in filename.lower():
                _format=".avi"
            if ".mov" in filename.lower():
                _format=".mov"
            if ".mkv" in filename.lower():
                _format=".mkv"
            inputfile = os.path.join(root, filename)

            print('[INFO] 1',inputfile)
            outputPath = root.replace(src , dst)
            if not os.path.exists(outputPath):
                os.makedirs(outputPath);
            
            outputfile = os.path.join(outputPath, filename.replace(_format, ".mp4"))
               
            if _format != '' and _format != '.mkv' :
                subprocess.call(['ffmpeg','-hwaccel_device' ,'0' ,'-hwaccel' ,'cuda' ,'-i' , inputfile ,'-vf' ,'scale=-1:720' ,'-c:v' ,'h264_nvenc' , '-cq' , '21' ,'-preset' ,'slow' ,outputfile])
                print(filename , 'Converted')
            if _format == '':
                shutil.copyfile(os.path.join(root,filename),os.path.join(outputPath,filename))
                print(filename , 'Copied')
            if _format == '.mkv' : 
                print(filename , 'Skiped')
        except:     
            print("An exception occurred")