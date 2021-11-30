import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from functools import reduce

run47 = pd.read_csv('run47.csv', sep=',')
run48 = pd.read_csv('run48.csv', sep=',')
run49 = pd.read_csv('run49.csv', sep=',')
run50 = pd.read_csv('run50.csv', sep=',')
run51 = pd.read_csv('run51.csv', sep=',')

run = [run47, run48, run49, run50, run51]

# result = pd.merge(run50, run51, how="outer", on=['Mutation'])
dataframe = reduce(lambda  left,right: pd.merge(left,right,on=['SPIKE GLYCOPROTEIN MUTATION'],
                                            how='outer'), run).fillna('0')
print(dataframe)
list = []
for i in dataframe['SPIKE GLYCOPROTEIN MUTATION']:
    list.append(i[6:])

dataframe = dataframe.drop(columns=['SPIKE GLYCOPROTEIN MUTATION'])

dataframe['SPIKE GLYCOPROTEIN MUTATION'] = list
dataframe = dataframe.set_index('SPIKE GLYCOPROTEIN MUTATION')
dataframe = dataframe.astype({"RUN 47": int, "RUN 48": int,
                              "RUN 49": int, "RUN 50": int, "RUN 51": int})
print(dataframe)
dataframe = dataframe.sort_values(by='RUN 50', ascending=False)
dataframe.to_excel('test.xlsx')
ax = plt.axes()
fig, ax = plt.subplots(figsize=(10,40))
ax.set_title('Frequency of Mutations of Spike Glycoprotein Samples from GSI Lab')
sns.heatmap(dataframe, xticklabels="auto", yticklabels=True, annot=True, cmap="YlGnBu", annot_kws={"fontsize":8}, ax=ax)
sns.set(font_scale=0.2)
plt.tight_layout()
plt.show()



# data = pd.read_csv('run50_perlocation.csv', sep=',')
#
# spike = []
# count = []
#
# for i,j in zip(data['Mutation'], data['Count']):
#     if 'Spike' in i:
#         spike.append(i[6:])
#         count.append(j)
#
# dataframe = pd.DataFrame()
#
# dataframe['Spike'] = spike
# dataframe['RUN 50'] = count
#
# dataframe = dataframe.set_index('Spike')
# dataframe = dataframe.sort_values(by='RUN 50', ascending=False)
# print(dataframe)