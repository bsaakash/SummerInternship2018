from UQpy.SampleMethods import MCMC
from UQpy.RunModel import RunModel
import numpy as np
import time

def Rosenbrock(x, params):
    return np.exp(-(100*(x[1]-x[0]**2)**2+(1-x[0])**2)/params[0])

t = time.time()
x = MCMC(dimension=2, pdf_proposal_type='Normal', pdf_target_type='joint_pdf',
         pdf_target=Rosenbrock, pdf_target_params=[20], algorithm='MMH', jump=100000, nsamples=15, seed=None)
t_MCMC = time.time()-t
print(t_MCMC)

t = time.time()
z = RunModel(cpu=1, model_type='python', model_script='python_model.py', dimension=2, samples=x.samples)
t_run = time.time()-t
print(t_run)

print('Samples',z.model_eval.samples)
print('Soluations',z.model_eval.QOI)