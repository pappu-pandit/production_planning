import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


from datetime import timedelta

data=pd.read_csv('test.csv')
print(data['start'])
# convert data str to datetime data type yyyy_mm__dd
data["start"]=pd.to_datetime(data["start"], format="%d/%m/%Y")
data["end"]=pd.to_datetime(data["end"], format="%d/%m/%Y")


print(data['start'])




#sort tasks by start date
data.sort_values("start",axis=0,ascending=True,inplace=True)
# reset index inplace
data.reset_index(drop=True,inplace=True)

#add duartion of column

data["duration"]=data["end"]-data["start"] + timedelta(days=1)

# add column: strat date of each task wrt project dat1
data["PastTime"] = data["start"] - data["start"][0]

# strat drawing
nrow = len(data)
plt.figure(num=1,figsize=[8,5],dpi=100)
bar_width=0.6

for i in range(nrow):
	i_rev=nrow - 1 -i
	# plot yhe last task first
	plt.broken_barh([(data["start"][i_rev],data["Duration"][i_rev])],(i - bar_width/2,bar_width),color='orange')
	plt.broken_barh([(data["start"][0],data["PastTime"][i_rev])],(i - bar_width/2,bar_width),color='#f2f2f2')


y_pos=np.arange(nrow)
plt.yticks(y_pos,labels=reversed(data["task"]))

#plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.grid(axis='x',which='major',lw=1)
plt.grid(axis='x',which='major',ls='--',lw=1)

plt.gcf().autofmt_xdate(rotation=0)

plt.savefig('gant.png')
plt.show()

