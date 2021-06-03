import os
import glob
import pandas as pd

# files                                                                         

df = pd.read_csv("C:/Users/Monica/Desktop/TFM/Aphasia/df_clean.csv")
 
for i in range(len(df)):
       file = glob.glob(f"""C:/Users/Monica/Desktop/TFM/Aphasia/Audios/{df['file'][i]}""", recursive=True)
       start=((pd.to_numeric(df['mark_start'][i]))/1000)
       end=((pd.to_numeric(df['mark_end'][i]))-(pd.to_numeric(df['mark_start'][i])))/1000
       os.system(f"""sox {file[0]} {file[0][:-4]}_{start}_{end}.wav trim {start} {end}""")
       #print(file[0])
       #print(i)
