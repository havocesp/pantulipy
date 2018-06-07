# Pantulipy: Pandas + Tulipy

Pandas over then Tulipy technical indicators library.

* Author: Daniel J. Umpierrez
* Version: 0.1.0
* License: MIT

## Description

This project is created to integrate **tulipy** functions with **Pandas** library.

## Requirements
 * pandas
 * tulipy
 
## Installation

### Linux

#### Debian based

```bash
# requirements installation
sudo apt-get update
sudo apt-get install python3-pandas python3-pip  python3-cython
sudo pip install --user tulipy
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
 * [ ] Write some documentation.
 * [ ] Write some tests.

## Changelog
### 0.1.1
 * Now *_tup* function fit ohlc size and fill nan values by using DataFrame *bfill* method
### 0.1.0
 * Initial version.
