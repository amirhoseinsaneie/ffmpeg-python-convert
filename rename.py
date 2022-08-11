import os
src = './mp4/WARD 3 REDACTED'
for root, dirs, filenames in os.walk(src, topdown=False):
    # print(filenames)

    for filename in filenames:
        try:

            if ".mp4" in filename.lower():
                print('[INFO] 1', filename)

                os.rename(os.path.join(root, filename), os.path.join(
                    root, filename.replace('REST OF VIDS' , 'Rest of vids')))
                

        except:
            print("An exception occurred")
