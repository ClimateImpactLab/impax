from __future__ import absolute_import
import csv
import xarray as xr
import pandas as pd
import numpy as np
from scipy.stats import multivariate_normal as mn

import warnings


def read_csvv(csvv_path):
    '''
    Returns the gammas and covariance matrix 
    
    Parameters
    ----------
    path: str_or_buffer
        path to csvv file

    Returns
    -------
    gamma : Gamma
        :py:class:`Gamma` object with median and VCV matrix indexed by prednames, covarnames, and outcomes

    '''

    data = {}

    with open(csvv_path, 'r') as fp:
        reader = csv.reader(fp)

        for row in reader:
            if row[0] == 'gamma':
                data['gamma'] = np.array([float(i) for i in reader.next()])
            if row[0] == 'gammavcv':
                data['gammavcv'] = np.array([float(i) for i in reader.next()])
            if row[0] == 'residvcv':
                data['residvcv'] = np.array([float(i) for i in reader.next()])
            if row[0] == 'prednames':
                data['prednames'] = [i.strip() for i in reader.next()]
            if row[0] == 'covarnames':
                data['covarnames'] = [i.strip() for i in reader.next()]
            if row[0] == 'outcome': 
                data['outcome'] =[cv.strip() for cv in reader.next()]

    index = pd.MultiIndex.from_tuples(zip(data['outcome'], data['prednames'], data['covarnames']), 
                                            names=['outcome', 'prednames', 'covarnames'])

    g = Gammas(data['gamma'], data['gammavcv'], index)

    return g 


def get_gammas(*args, **kwargs):
    warnings.warn('get_gammas has been deprecated, and has been replaced with read_csvv', DeprecationWarning)
    return read_csvv(*args, **kwargs)


class Gammas(object):
    '''
    Stores a median and residual VCV matrix for multidimensional variables with named indices
    and provides multivariate sampling and statistical analysis functions

    Parameters
    ----------
    gammas: array 
        length $(m1*m2*...*mn)$ 1-d :py:class:`~numpy.array` with median values for multivariate distribution

    gammavcv: array
        $(m1*m2*...*mn)x(m1*m2*...*mn)$ :py:class:`~numpy.array` with covariance matrix for multivariate distribution

    index: MultiIndex
        $(m1*m2*...*mn)$ 1-d :py:class:`~pandas.MultiIndex` describing the multivariate space
    
    '''

    def __init__(self, gammas, gammavcv, index):
        self.gammas = gammas
        self.gammavcv = gammavcv
        self.index = index

    def median(self):
        '''
        Returns the values in the array of gammas organized according to specification

        Returns
        -------
        median : xarray.DataArray
            :py:class `~xarray.DataArray` of gamma coefficients organized by covar and pred
        '''

        return pd.Series(self.gammas, index=self.index).to_xarray()

    def sample(self, seed=None):
        '''
        Takes a draw from a multivariate distribution and returns a Dataset of coefficients. 
        Labels on coefficients can be used to construct a specification of the functional form.

        Returns
        ----------
        draw : xarray.DataArray
            :py:class:`~xarray.DataArray` of parameter estimates drawn from the multivariate normal

        '''
        if seed is not None:
            warnings.warn('Sampling with a seed has been deprecated. In future releases, this will be up to the user.', DeprecationWarning)
            np.random.seed(seed)

        return pd.Series(mn.rvs(self.gammas, self.gammavcv), index=self.index).to_xarray()
