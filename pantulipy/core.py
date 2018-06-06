# -*- coding:utf-8 -*-
import inspect as insp

import pandas as pd
import tulipy
from tulipy.lib import _Indicator

_OHLCV = ['open', 'high', 'low', 'close', 'volume']
_FUNCS = sorted([f for f in dir(tulipy) if f[0].islower() and 'lib' not in f])
_FUNCTIONS_REFERENCES = {fn: n for n, fn in enumerate(_FUNCS)}

__all__ = ['ad', 'adosc', 'adx', 'adxr', 'ao', 'apo', 'aroon', 'aroonosc', 'atr', 'avgprice', 'bbands', 'bop', 'cci',
           'cmo', 'crossany', 'crossover', 'cvi', 'decay', 'dema', 'di', 'dm', 'dpo', 'dx', 'edecay', 'ema', 'emv',
           'fisher', 'fosc', 'hma', 'kama', 'kvo', 'lag', 'linreg', 'linregintercept', 'linregslope', 'macd',
           'marketfi', 'mass', 'md', 'mfi', 'mom', 'msw', 'natr', 'nvi', 'obv', 'ppo', 'psar', 'pvi', 'qstick',
           'roc', 'rocr', 'rsi', 'sma', 'stderr', 'stoch', 'tema', 'tr', 'trima', 'trix', 'tsf', 'typprice', 'ultosc',
           'vhf', 'vidya', 'volatility', 'vosc', 'vwma', 'wad', 'wcprice', 'wilders', 'willr', 'wma', 'zlema']


def _get_ohlcv_arrays(fn, ohlc):
    sign = list(insp.signature(fn).parameters.keys())
    params = ['close' if 'real' in p else p for p in sign if p in _OHLCV]
    return ohlc[params].T.values


def _tup(fn, ohlc, *args, **kwargs):
    """
    Calculate any function from "Tulipy" library from a OHLC Pandas DataFrame.

    :param function fn: the "Tulipy" function to call
    :param pd.DataFrame ohlc: a Pandas DataFrame type with open, high, low, close and or volume columns.
    :param args: function positional params.
    :param kwargs: function key pair params.
    :return pd.Series: a Pandas Series with data result.
    """
    fn_params = list(args) + list(kwargs.values())
    fn_name = fn.__name__.upper()
    data = fn(*_get_ohlcv_arrays(fn, ohlc), *fn_params)
    return pd.Series(data, index=ohlc.index, name=fn_name)


def ad(data):
    """
    Accumulation/Distribution Line.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ad'), data)


def adosc(data, short_period, long_period):
    """
    Accumulation/Distribution Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'adosc'), data, short_period, long_period)


def adx(data, period):
    """
    Average Directional Movement Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'adx'), data, period)


def adxr(data, period):
    """
    Average Directional Movement Rating.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'adxr'), data, period)


def ao(data):
    """
    Awesome Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ao'), data)


def apo(data, short_period, long_period):
    """
    Absolute Price Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'apo'), data, short_period, long_period)


def aroon(data, period):
    """
    Aroon.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'aroon'), data, period)


def aroonosc(data, period):
    """
    Aroon Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'aroonosc'), data, period)


def atr(data, period):
    """
    Average True Range.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'atr'), data, period)


def avgprice(data):
    """
    Average Price.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'avgprice'), data)


def bbands(data, period, stddev):
    """
    Bollinger Bands.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :param stddev: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'bbands'), data, period, stddev)


def bop(data):
    """
    Balance Of Power.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'bop'), data)


def cci(data, period):
    """
    Commodity Channel Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'cci'), data, period)


def cmo(data, period):
    """
    Chande Momentum Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'cmo'), data, period)


def crossany(data):
    """
    Crossany.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'crossany'), data)


def crossover(data):
    """
    Crossover.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'crossover'), data)


def cvi(data, period):
    """
    Chaikins Volatility.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'cvi'), data, period)


def decay(data, period):
    """
    Linear Decay.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'decay'), data, period)


def dema(data, period):
    """
    Double Exponential Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'dema'), data, period)


def di(data, period):
    """
    Directional Indicator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'di'), data, period)


def dm(data, period):
    """
    Directional Movement.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'dm'), data, period)


def dpo(data, period):
    """
    Detrended Price Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'dpo'), data, period)


def dx(data, period):
    """
    Directional Movement Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'dx'), data, period)


def edecay(data, period):
    """
    Exponential Decay.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'edecay'), data, period)


def ema(data, period):
    """
    Exponential Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ema'), data, period)


def emv(data):
    """
    Ease Of Movement.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'emv'), data)


def fisher(data, period):
    """
    Fisher Transform.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'fisher'), data, period)


def fosc(data, period):
    """
    Forecast Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'fosc'), data, period)


def hma(data, period):
    """
    Hull Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'hma'), data, period)


def kama(data, period):
    """
    Kaufman Adaptive Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'kama'), data, period)


def kvo(data, short_period, long_period):
    """
    Klinger Volume Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'kvo'), data, short_period, long_period)


def lag(data, period):
    """
    Lag.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'lag'), data, period)


def linreg(data, period):
    """
    Linear Regression.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'linreg'), data, period)


def linregintercept(data, period):
    """
    Linear Regression Intercept.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'linregintercept'), data, period)


def linregslope(data, period):
    """
    Linear Regression Slope.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'linregslope'), data, period)


def macd(data, short_period, long_period, signal_period):
    """
    Moving Average Convergence/Divergence.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :param signal_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'macd'), data, short_period, long_period, signal_period)


def marketfi(data):
    """
    Market Facilitation Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'marketfi'), data)


def mass(data, period):
    """
    Mass Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'mass'), data, period)


def md(data, period):
    """
    Mean Deviation Over Period.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'md'), data, period)


def mfi(data, period):
    """
    Money Flow Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'mfi'), data, period)


def mom(data, period):
    """
    Momentum.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'mom'), data, period)


def msw(data, period):
    """
    Mesa Sine Wave.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'msw'), data, period)


def natr(data, period):
    """
    Normalized Average True Range.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'natr'), data, period)


def nvi(data):
    """
    Negative Volume Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'nvi'), data)


def obv(data):
    """
    On Balance Volume.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'obv'), data)


def ppo(data, short_period, long_period):
    """
    Percentage Price Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ppo'), data, short_period, long_period)


def psar(data, acceleration_factor_step, acceleration_factor_maximum):
    """
    Parabolic Sar.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param acceleration_factor_step: TODO
    :param acceleration_factor_maximum: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'psar'), data, acceleration_factor_step, acceleration_factor_maximum)


def pvi(data):
    """
    Positive Volume Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'pvi'), data)


def qstick(data, period):
    """
    Qstick.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'qstick'), data, period)


def roc(data, period):
    """
    Rate Of Change.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'roc'), data, period)


def rocr(data, period):
    """
    Rate Of Change Ratio.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'rocr'), data, period)


def rsi(data, period):
    """
    Relative Strength Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'rsi'), data, period)


def sma(data, period):
    """
    Simple Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'sma'), data, period)


def stderr(data, period):
    """
    Standard Error Over Period.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'stderr'), data, period)


def stoch(data, pct_k_period, pct_k_slowing_period, pct_d_period):
    """
    Stochastic Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param %k_period: TODO
    :param %k_slowing_period: TODO
    :param %d_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'stoch'), data, pct_k_period, pct_k_slowing_period, pct_d_period)


def tema(data, period):
    """
    Triple Exponential Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'tema'), data, period)


def tr(data):
    """
    True Range.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'tr'), data)


def trima(data, period):
    """
    Triangular Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'trima'), data, period)


def trix(data, period):
    """
    Trix.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'trix'), data, period)


def tsf(data, period):
    """
    Time Series Forecast.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'tsf'), data, period)


def typprice(data):
    """
    Typical Price.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'typprice'), data)


def ultosc(data, short_period, medium_period, long_period):
    """
    Ultimate Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param medium_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ultosc'), data, short_period, medium_period, long_period)


def vhf(data, period):
    """
    Vertical Horizontal Filter.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'vhf'), data, period)


def vidya(data, short_period, long_period, alpha):
    """
    Variable Index Dynamic Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :param alpha: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'vidya'), data, short_period, long_period, alpha)


def volatility(data, period):
    """
    Annualized Historical Volatility.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'volatility'), data, period)


def vosc(data, short_period, long_period):
    """
    Volume Oscillator.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'vosc'), data, short_period, long_period)


def vwma(data, period):
    """
    Volume Weighted Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'vwma'), data, period)


def wad(data):
    """
    Williams Accumulation/Distribution.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'wad'), data)


def wcprice(data):
    """
    Weighted Close Price.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'wcprice'), data)


def wilders(data, period):
    """
    Wilders Smoothing.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'wilders'), data, period)


def willr(data, period):
    """
    Williams %R.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'willr'), data, period)


def wma(data, period):
    """
    Weighted Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'wma'), data, period)


def zlema(data, period):
    """
    Zero-Lag Exponential Moving Average.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'zlema'), data, period)


# if __name__ == '__main__':

#
#     print([*map(str.lower, desired_funcs)])
if __name__ == '__main__':

    desired_funcs = ['AD', 'ADOSC', 'ADX', 'ADXR', 'AO', 'APO', 'AROON', 'AROONOSC', 'ATR', 'AVGPRICE', 'BBANDS', 'BOP',
                     'CCI', 'CMO', 'CROSSANY', 'CROSSOVER', 'CVI', 'DECAY', 'DEMA', 'DI', 'DM', 'DPO', 'DX', 'EDECAY',
                     'EMA', 'EMV', 'FISHER', 'FOSC', 'HMA', 'KAMA', 'KVO', 'LAG', 'LINREG', 'LINREGINTERCEPT',
                     'LINREGSLOPE', 'MACD', 'MARKETFI', 'MASS', 'MD', 'MFI', 'MOM', 'MSW', 'NATR', 'NVI', 'OBV',
                     'PPO', 'PSAR', 'PVI', 'QSTICK', 'ROC', 'ROCR', 'RSI', 'SMA', 'STDERR', 'STOCH', 'TEMA',
                     'TR', 'TRIMA', 'TRIX', 'TSF', 'TYPPRICE', 'ULTOSC', 'VHF', 'VIDYA', 'VOLATILITY', 'VOSC', 'VWMA',
                     'WAD', 'WCPRICE', 'WILDERS', 'WILLR', 'WMA', 'ZLEMA']
    #
    # pprint([fn for fn in dir(importlib.import_module(__name__)) if '_' not in fn[0] and fn.isupper()])
    doc_string = """
def {name}(data{options}):
    '''
    {full}.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).{params}
    :return pd.Series: indicator results as pandas Series instance.
    '''
    return tup(getattr(tulipy, '{name}'), data{options})
    """
    for fn in desired_funcs:

        ref = _FUNCTIONS_REFERENCES.get(fn.lower())
        if not isinstance(ref, int): continue
        f = _Indicator(ref)
        fn = str(f.name, encoding='utf-8')
        full_name = str(f.full_name, encoding='utf-8')
        option_params = [str(s, encoding='utf-8') for s in f.options]
        options = ', ' + ', '.join([s.strip().replace(' ', '_') for s in option_params]) if len(option_params) else ''
        params = []
        params_doc = '\n'.join(["    :param {opt}: TODO""".format(opt=opt.strip().replace(' ',
                                                                                          '_')) if opt != 'period' else "    :param int {opt}: number of period used for indicators calcs.""".format(
            opt=opt) for opt in option_params])
        if len(params_doc):
            params_doc = '\n' + params_doc
        print(doc_string.format(full=full_name.title(), params=params_doc, name=fn,
                                options=options.replace('\n', '')).replace("'''", '"""'))

# 'def {fn}(data, *args, **kwargs):\n    \n    """\n    {full}\n\n    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).\n    :return pd.Series: indicator results as pandas Series instance.\n    """\n    return tup({fn}, data, *args, **kwargs)\n\n'.format(
#     fn=fn.upper(), full=full_name.title()))
