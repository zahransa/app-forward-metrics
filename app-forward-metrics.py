# Import some libraries
import matplotlib.pyplot as plt
from pandas import np
from scipy import linalg
import scipy.io


# Read the lead field matrix
mat = scipy.io.loadmat('ga.mat')
gain=mat["gaina"]