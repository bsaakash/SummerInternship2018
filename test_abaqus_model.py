from UQpy.SampleMethods import MCS
from UQpy.RunModel import RunModel
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import time

t = time.time()
x = MCS(dimension=1, icdf=['Normal'], icdf_params=[[0,1]], nsamples=5)
mu = 70e9
sigma = 1e9
# x = y
x.samples = mu + x.samples*sigma
t_MCS = time.time()-t
print(t_MCS)
print(x.samples)