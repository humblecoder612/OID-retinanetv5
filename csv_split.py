import pandas as pd
ANOT_PATH="/storage/research/Intern19_v2/DetectObjectsInVariedAndComplexImages/labelScript.csv"
import time
anot=pd.read_csv(ANOT_PATH)
anot1=anot.iloc[:10000,:]
print("file1 done",anot.shape)
time.sleep(2)
anot2=anot.iloc[10000:20000,:]
print("file 2 done",anot2.shape)
time.sleep(2)
anot3=anot.iloc[20000:30000,:]
print("file 3 done",anot3.shape)
time.sleep(2)
anot1.to_csv("Label1.csv",index=False,header=False)
anot2.to_csv("Label2.csv",index=False,header=False)
anot3.to_csv("Label3.csv",index=False,header=False)
