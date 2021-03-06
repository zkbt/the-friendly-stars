# basic tools
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
import warnings, os, copy, glob
from tqdm import tqdm

# some standard astropy tools
import astropy.units as u
from astropy.coordinates import SkyCoord
import astropy.io.fits
astropy.io.fits.conf.use_memmap = False
from astropy.io import fits, ascii
from astropy.wcs import WCS
from astropy.time import Time
from astropy.table import Table, QTable
from astropy.stats import mad_std
from matplotlib.transforms import Affine2D

import pickle

# a handy tool for speaking classes
from .talker import Talker

def mkdir(path):
        '''
        A mkdir that doesn't complain if it already exists.
        '''
        try:
            os.mkdir(path)
            print("made {}".format(path))
        except:
            pass
