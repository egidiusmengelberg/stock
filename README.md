# Stock prediction using python

## Contents

- [Contents](#contents)
- [Requirements/Installation](#requirements/installation)
- [Usage](#usage)
- [Explanation](#explanation)

## Requirements/Installation
This software will only work with python3 3+!

To install all the required python packages run the following command:

```bash
pip3 install -r requirements.txt
```

The other thing you will need are all the historical prices from the S&P500.
Luckily someone named Sentdex already collected all these files. These can be downloaded from:

[Historical stock prices](https://pythonprogramming.net/data-acquisition-machine-learning/)

On his page you will find a file named `intraQuarter.zip`, which you should download, unzip, and place in your working directory.

After that you can finally use the software!

## Usage

To use this code please run the following commands in this order.

```bash
python download_historical_prices.py
python parsing_keystats.py
python current_data.py
python backtesting.py
python stock_prediction.py
```

## Explanation

### download_historical_prices.py

```bash
python download_historical_prices.py
```

This file will download all the historical prices from yahoo finance.


### parsing_keystats.py

```bash
python parsing_keystats.py
```

This file will parse the collected html pages using regex. (Could be improved with BeautifulSoup.)

### current_data.py

```bash
python current_data.py
```

This file will collect the current data and parse it the same way as parse_keystats.py.

### backtesting.py

```bash
python backtesting.py
```

This file will split the training data and train on the first half. The second half is used to simulate trading.
After trading it will return how succesful it was.

### stock_prediction.py

```bash
python stock_prediction.py
```

This file will return all the S&P500 companies which will outperform by a set ammount. This ammount can be adjusted in the config. (Default is 15%.)


