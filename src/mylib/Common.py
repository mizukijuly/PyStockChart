import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import yfinance as yf
import mplfinance as mpf

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


figSizeHeight = 3
figSizeWidth = 4


class data:
    dataframe = 0

def GetData(ticker, data):
    rawData = yf.download(ticker , period='1y', interval = "1d")
    data.dataframe = rawData
    print(data.dataframe)

def DrawPlot(data, frame):    
    data.dataframe = data.dataframe.drop("Volume", axis=1)
    fig = plt.figure(figsize=(figSizeWidth, figSizeHeight))
    ax = fig.add_subplot(1, 1, 1)
    data.dataframe.plot(ax=ax)
    canvas = FigureCanvasTkAgg(fig, frame)  # Generate canvas instance, Embedding fig in frame
    canvas.get_tk_widget().pack()
    canvas._tkcanvas.pack()

def DrawCandle(data, frame):
    fig, axlist = mpf.plot(data.dataframe, type="candle", volume=True,figratio=(10,5), returnfig=True)
    fig.set_size_inches(figSizeWidth, figSizeHeight)
    canvas = FigureCanvasTkAgg(fig, frame)  # Generate canvas instance, Embedding fig in frame
    canvas.get_tk_widget().pack()
    canvas._tkcanvas.pack()