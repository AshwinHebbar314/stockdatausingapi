#%%
import datetime
# %%
f = open('dataset.txt', 'r')
op = eval(f.readline())

output = open("outputdata.csv" , 'w')
#%%
idxs = "Date,"
for i in range(0,5):
    idxs += str(op[i]['Meta Data']['2. Symbol']) + ','
output.writelines(idxs.strip(',') + '\n')

#%%

for j in range(200):
    edxs = ""
    for i in range(0,5):
        try:
            edxs += str(op[i]['Weekly Time Series'][str(datetime.date(2021,9,10)-datetime.timedelta(7*j))]['4. close']) + ","
        except KeyError:
            edxs += 'NaN' + ','
        #print(str(datetime.date(2021,9,10)-datetime.timedelta(7*j)))
    outstr = str(datetime.date(2021,9,10)-datetime.timedelta(7*j))+ ',' + edxs.strip(',') + '\n'
    output.writelines(outstr)

# %%
f.close()
output.close()
# %%
