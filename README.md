# Pantulipy: Pandas + Tulipy

Pandas over then Tulipy technical indicators library.

* Author: Daniel J. Umpierrez
* Version: 0.1.3
* License: UNLICENSE

## Description

This project is created to integrate **newtulipy** functions with **Pandas** library.

## Requirements
 * cython
 * numpy
 * pandas
 * newtulipy
 
## Installation

### Linux

#### Debian based

```bash
# requirements installation
sudo apt-get update
sudo apt-get install python3-numpy python3-pandas python3-pip  python3-cython cython3
pip3 install newtulipy
pip3 install git+https://github.com/havocesp/pantulipy
```

## Usage

Just import needed functions and call.

```python
import pandas as pd
from pantulipy import ema

# replace this by your OHLC DataFrame
ohlc_data = pd.DataFrame()
print(ema(ohlc_data, 5).tail())
```

## TODO
 * [ ] Implement class with functions.
 * [x] Write some documentation.
 * [ ] Write some tests.

## Changelog

### 0.1.3
 * Cython and numpy added as dependencies.
 * Replace tulipy with newtulipy.
### 0.1.2
 * Added most common default values for many functions.
 * Some code refactor.
 * Added "requirements.txt" file.
### 0.1.1
 * Now *_tup* function fit ohlc size and fill nan values by using DataFrame *bfill* method
### 0.1.0
 * Initial version.
