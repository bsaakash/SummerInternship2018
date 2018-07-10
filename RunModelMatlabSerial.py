from UQpy.SampleMethods import MCMC
from UQpy.RunModel import RunModel
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import time

def Rosenbrock(x, params):
    return np.exp(-(100*(x[1]-x[0]**2)**2+(1-x[0])**2)/params[0])

t = time.time()
x = MCMC(dimension=2, pdf_proposal_type='Normal', pdf_target_type='joint_pdf',
         pdf_target=Rosenbrock, pdf_target_params=[20], algorithm='MMH', jump=100, nsamples=15, seed=None)
t_MCMC = time.time()-t
print(t_MCMC)

np.savetxt('UQpy_Samples.txt', x.samples, fmt='%0.5f')

t = time.time()
z = RunModel(cpu=1, model_type=None, model_script='UQpy_Model.sh',
             input_script='UQpy_Input.sh', output_script='UQpy_Output.sh',
             dimension=2)
t_run = time.time()-t
print(t_run)

print('Samples',z.model_eval.samples)
print('Soluations',z.model_eval.QOI)