#! /bin/sh

# export PATH=$PATH:/Applications/MATLAB_R2017a.app/bin/
"/mnt/c/Program Files/MATLAB/R2018a/bin/matlab.exe" -nodisplay -nosplash -nodesktop -nojvm -r "matlab_model($1);exit()" &

# until [ -f ./done.txt ]
# do
	# sleep 1
# done
echo "File found."

#python python_model.py $1




