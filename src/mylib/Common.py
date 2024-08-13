import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import yfinance as yf


def GetData(ticker):
    data = yf.download(ticker , period='5d', interval = "1d")
    df = data
    df = df.drop("Volume", axis=1)
    
    return df