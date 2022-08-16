# -*- coding:utf-8 -*-
"""
    Pantulipy: a Pandas over then Tulipy technical indicators library.
"""
import os
import sys

# global debug flag
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

globals().update(BASE_DIR=BASE_DIR)
globals().update(DEBUG=DEBUG)

sys.path.append(BASE_DIR)

from .core import (ad, adosc, adx, adxr, ao, apo, aroon, aroonosc, atr, avgprice, bbands, bop, cci, cmo, crossany,
                  crossover, cvi, decay, dema, di, dm, dpo, dx, edecay, ema, emv, fisher, fosc, hma, kama, kvo, lag,
                  linreg, linregintercept, linregslope, macd, marketfi, mass, md, mfi, mom, msw, natr, nvi, obv, ppo,
                  psar, pvi, qstick, roc, rocr, rsi, sma, stderr, stoch, tema, tr, trima, trix, tsf, typprice, ultosc,
                  vhf, vidya, volatility, vosc, vwma, wad, wcprice, wilders, willr, wma, zlema, InvalidOptionError)

__version__ = '0.1.1'
__author__ = 'Daniel J. Umpierrez'
__license__ = 'UNLICENSE'
__package__ = 'pantulipy'
__description__ = 'A Pandas over then Tulipy technical indicators library.'
__site__ = 'https://github.com/havocesp/' + __package__
__email__ = 'umpierrez@pm.me'
__dependencies__ = [
    'tulipy',
    'pandas'
]

__keywords__ = ['pantulipy', 'tulipy', 'technical-analisys', 'indicator', 'indicators', 'pandas', 'python', 'finance',
                'exchange', 'stock', 'bitcoin', 'crypto-currencies', 'cryptocurrencies', 'altcoin', 'altcoins']


__all__ = ['__version__', '__author__', '__license__', '__package__', '__description__', '__site__', '__email__',
           '__dependencies__', '__keywords__', 'ad', 'adosc', 'adx', 'adxr', 'ao', 'apo', 'aroon', 'aroonosc', 'atr',
           'avgprice', 'bbands', 'bop', 'cci', 'cmo', 'crossany', 'crossover', 'cvi', 'decay', 'dema', 'di', 'dm',
           'dpo', 'dx', 'edecay', 'ema', 'emv', 'fisher', 'fosc', 'hma', 'kama', 'kvo', 'lag', 'linreg',
           'linregintercept', 'linregslope', 'macd', 'marketfi', 'mass', 'md', 'mfi', 'mom', 'msw', 'natr', 'nvi',
           'obv', 'ppo', 'psar', 'pvi', 'qstick', 'roc', 'rocr', 'rsi', 'sma', 'stderr', 'stoch', 'tema', 'tr', 'trima',
           'trix', 'tsf', 'typprice', 'ultosc', 'vhf', 'vidya', 'volatility', 'vosc', 'vwma', 'wad', 'wcprice',
           'wilders', 'willr', 'wma', 'zlema', 'InvalidOptionError']
