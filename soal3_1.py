import matplotlib.pyplot as plt
import pandas as pd
import os 
from flask import Flask
import numpy as np
import matplotlib.dates as mdates

# The converter was registered by pandas on import
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#folder to save file
app=Flask(__name__)
app.config['UPLOAD_FOLDER']='./chart'

#Dataframe from csv
xl=pd.read_csv('./dataSaham/EXCL.JK.csv',parse_dates=['Date'])
xl=xl.set_index('Date')
smartfren=pd.read_csv('./dataSaham/FREN.JK.csv',parse_dates=['Date'])
smartfren=smartfren.set_index('Date')
isat=pd.read_csv('./dataSaham/ISAT.JK.csv',parse_dates=['Date'])
isat=isat.set_index('Date')
tlkm=pd.read_csv('./dataSaham/TLKM.JK.csv',parse_dates=['Date'])
tlkm=tlkm.set_index('Date')

#Plot
plt.figure(figsize=(12,7))
plt.style.use('ggplot')
plt.plot(xl.index,xl['Close'],'g-',
        smartfren.index,smartfren['Close'],'r-',
        isat.index,isat['Close'],'b-',
        tlkm.index,tlkm['Close'],'purple')
plt.grid(True)
plt.legend(['PT XL Axiata Tbk','PT Smartfren Telecom Tbk','PT Indosat Tbk','PT Telekomunikasi Indonesia Tbk'],loc='upper center',ncol=4,fontsize=7,bbox_to_anchor=(0.5, 1.05))
plt.title('Harga Historis Saham Provider Telco Indonesia\n\n')
plt.ylabel('Rupiah (IDR)',fontsize=9)
plt.xlabel('Tanggal',fontsize=9)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.xticks(np.arange(np.datetime64('2019-03-16'), np.datetime64('2019-06-14'),7),rotation=65,fontsize=7)
plt.yticks(fontsize=7)
namafile='soal3_1.png'
plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'],namafile))
plt.show()

