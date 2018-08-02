from abaqus import *
import job
import sys

jobname = mdb.JobFromInputFile(sys.argv[-1], sys.argv[-1]+".inp")
jobname.submit()
jobname.waitForCompletion()