from posixpath import dirname
import subprocess
import os
import shutil
src = './src'
dst = './mp4'

for root, dirs, filenames in os.walk(src, topdown=False):
    #print(filenames)

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

            inputfile = os.path.join(root, filename)

            print('[INFO] 1',inputfile)
            outputPath = root.replace(src , dst)
            if not os.path.exists(outputPath):
                os.makedirs(outputPath);
                outputfile = os.path.join(outputPath, filename.lower().replace(_format, ".mp4"))
                # subprocess.call(['ffmpeg', '-i', inputfile, '-vf','scale=-1:720', '-c:v', 'h264_nvenc', '-crf', '25', '-preset' ,'veryslow' ,'-c:a' ,'copy' , outputfile])  
                if _format != '' :
                    subprocess.call(['ffmpeg','-hwaccel_device' ,'0' ,'-hwaccel' ,'cuda' ,'-i' , inputfile ,'-vf' ,'scale=-1:720' ,'-c:v' ,'h264_nvenc' ,'-preset' ,'slow' ,outputfile])
                if not ".avi" in filename.lower():
                    shutil.copyfile(os.path.join(root,filename),os.path.join(outputPath,filename))
                    print(filename , 'Copied')
            else:
                break;
        except:     
            print("An exception occurred")