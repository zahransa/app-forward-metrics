import numpy as np
import mne
from mne.datasets import sample
from mne.source_space import compute_distance_to_sensors
from mne.source_estimate import SourceEstimate
import matplotlib.pyplot as plt

print(__doc__)

data_path = sample.data_path()
meg_path = data_path / 'MEG' / 'sample'
fwd_fname = meg_path / 'sample_audvis-meg-eeg-oct-6-fwd.fif'
subjects_dir = data_path / 'subjects'

# Read the forward solutions with surface orientation
fwd = mne.read_forward_solution(fwd_fname)
mne.convert_forward_solution(fwd, surf_ori=True, copy=False)
leadfield = fwd['sol']['data']
print("Leadfield size : %d x %d" % leadfield.shape)

grad_map = mne.sensitivity_map(fwd, ch_type='grad', mode='fixed')
mag_map = mne.sensitivity_map(fwd, ch_type='mag', mode='fixed')
eeg_map = mne.sensitivity_map(fwd, ch_type='eeg', mode='fixed')

