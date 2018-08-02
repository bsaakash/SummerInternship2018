from UQpy.SampleMethods import MCS
from UQpy.RunModel import RunModel
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import time

t = time.time()
#x = MCS(dimension=1, icdf=['Normal'], icdf_params=[[0,1]], nsamples=3)
mu1 = 70e9
sigma1 = 1e9
mu2 = 0.0254
sigma2 = 0.00254
# x = y
#x.samples = mu + x.samples*sigma
x = MCS(dimension=2, icdf=['Normal','Normal'], icdf_params=[[mu1,sigma1],[mu2,sigma2]], nsamples=20)
t_MCS = time.time()-t
print(t_MCS)
print(x.samples)

np.savetxt('UQpy_Samples.txt', x.samples, fmt='%0.5f')

t = time.time()
z = RunModel(cpu=1, model_type=None, model_script='UQpy_Model.py', input_script='UQpy_Input.py', output_script='UQpy_Output.py',
             dimension=1)
t_run = time.time()-t
print(t_run)

print('Samples: \n',z.model_eval.samples)
print('Solutions: \n',z.model_eval.QOI)