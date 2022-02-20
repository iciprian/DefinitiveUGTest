import os
import pandas as pd  
# This is to get the directory that the program 
# is currently running in.
dir_path = os.path.dirname(os.path.realpath(__file__))

T = []

for root, dirs, files in os.walk('/home/icipriano/OmpWomp_Feb9'):
    for file in files:
        if file.endswith('.out'):
            # print (root+'/'+str(file))
            filename=root+'/'+str(file)
            file1 = open(filename, "r")
            L = [file.split('_')[-1].split('.')[0]]
            for line in file1:
                if 'BZ_NITERATIONS' in line:
                    L.append(int(line.rsplit(' ',1)[-1]))
                if 'BZ_SOLVETIME' in line:
                    L.append(float(line.rsplit(' ',1)[-1]))

                #if 'BZ_UBOUND' in line:
                 #   L.append(float(line.rsplit(' ',1)[-1]))

                #if 'BZ_LBOUND' in line:
                 #   L.append(float(line.rsplit(' ',1)[-1]))    

                if 'TOPOSORT_OBJVAL' in line:
                    L.append(float(line.rsplit(' ',1)[-1]))
                    
            T.append(L)
df = pd.DataFrame(columns=('INSTANCE','BZ_NITERATIONS','BZ_SOLVETIME','TOPOSORT_OBJVAL'))
for i in range(len(T)):
    if len(T[i])==4:
        df.loc[i] = T[i]
    else:    
        print(T[i])
print(df.sort_values(by=['INSTANCE']))            
