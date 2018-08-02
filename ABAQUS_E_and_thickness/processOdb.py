#from abaqus import *
from odbAccess import *
import sys

jobname = sys.argv[-2] + ".odb"
index = sys.argv[-1]
# index = 1
#job_prefix = "LBA_beam_"
# jobname = os.path.join(os.getcwd(),job_prefix+str(index)) #TODO: pick the correct jobname automatically
#jobname = job_prefix+str(index)+'.odb'


print("Opening odb:")
print(jobname)

print("Index:")
print(index)


a1 = openOdb(jobname)
f1 = a1.steps['buckle'].frames[2].description
# e1 = float(f1[-11:])
e1 = f1[-11:]
a1.close()

filename = "UQpy_eval_"+str(index)+".txt"
with open(filename, "w") as f: 
    f.write(e1) 

# s1 = a1.steps['Step-1'].frames[1].description
# e1 = s1[-6:-1]
