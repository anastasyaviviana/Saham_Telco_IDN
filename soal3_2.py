import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

# The converter was registered by pandas on import
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#Data saham bulan Maret - Juni 2019
xl=pd.read_csv('./dataSaham/EXCL.JK.csv',parse_dates=['Date'])
xl=xl.set_index('Date')
smartfren=pd.read_csv('./dataSaham/FREN.JK.csv',parse_dates=['Date'])
smartfren=smartfren.set_index('Date')
isat=pd.read_csv('./dataSaham/ISAT.JK.csv',parse_dates=['Date'])
isat=isat.set_index('Date')
tlkm=pd.read_csv('./dataSaham/TLKM.JK.csv',parse_dates=['Date'])
tlkm=tlkm.set_index('Date')

#Data saham bulan April
xlapril=xl['2019-04']
smartfrenapril=smartfren['2019-04']
isatapril=isat['2019-04']
tlkmapril=tlkm['2019-04']

#Plot
plt.style.use('ggplot')
plt.figure(figsize=(9,6))
plt.plot(xlapril.index,xlapril['Close'],'g-',
        smartfrenapril.index,smartfrenapril['Close'],'r-',
        isatapril.index,isatapril['Close'],'b-',
        tlkmapril.index,tlkmapril['Close'],'purple')
plt.grid(True)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.xticks(rotation=65,fontsize=7)
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.legend(['PT XL Axiata Tbk','PT Smartfren Telecom Tbk','PT Indosat Tbk','PT Telekomunikasi Indonesia Tbk'],loc='upper center',ncol=4,fontsize=7,bbox_to_anchor=(0.5, 1.06))
plt.title('Harga Historis Saham Provider Telco Indonesia (April 2019)\n\n')
plt.show()