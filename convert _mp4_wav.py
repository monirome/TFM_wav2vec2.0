import os
import glob
# files                                                                         
lst = glob.glob("C:/Users/Monica/Desktop/TFM/Aphasia/Audios/originales/*.mp4", recursive=True)
print(lst)
 
for file in lst:
    os.system(f"""ffmpeg -i {file} -ar 16000 -ac 1 {file[:-4]}.wav""") 
