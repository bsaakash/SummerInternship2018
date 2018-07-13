#! /bin/sh

# export PATH=$PATH:/Applications/MATLAB_R2017a.app/bin/
# matlab -nodisplay -nodesktop -r "run matlab_model($1); exit"

# python python_model.py $1


import matlab.engine
import sys

ind = sys.argv[1]
eng = matlab.engine.start_matlab()
eng.matlab_model(int(ind), nargout=0)
eng.quit()