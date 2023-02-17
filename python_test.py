import pandas as pd

#a):
vuelosDf = pd.read_csv(r'vuelos.csv')
pilotosDf = pd.read_csv(r'pilotos.csv',encoding='cp1252')

#b) y c):
##Df que contiene el nombre del piloto
mergedDf=pd.merge(vuelosDf, pilotosDf , on='Codigo Piloto')
#mergedDf.to_csv('output_B_C.csv')


#d):
mergedDf = mergedDf.drop(mergedDf[mergedDf['Origen'] == mergedDf['Destino']].index)
#mergedDf.to_csv('output_D.csv')

#e):
mergedDf.loc[mergedDf['Minutos de retraso'].abs() <= 30, 'OnTime'] = 'A'
mergedDf.loc[(mergedDf['Minutos de retraso'].abs() > 30) & (mergedDf['Minutos de retraso'].abs() <=50),'OnTime'] = 'B'
mergedDf.loc[mergedDf['Minutos de retraso'].abs() > 50, 'OnTime'] = 'C'
mergedDf.to_csv('output_E.csv')
print(mergedDf)


#f) Jonh Pierson
#mergedDf[(mergedDf['Ontime'] == 'A') ].sum()
df_count_piloto = mergedDf.groupby('Piloto')['OnTime'].apply(lambda y: (y=='A').sum()).reset_index(name='count')
df_count_piloto = df_count_piloto.sort_values(by=['count'],ascending=False)
print(df_count_piloto)


#g) Aerolinea 4
#mergedDf[(mergedDf['Ontime'] == 'A') ].sum()
df_count_aerolinea = mergedDf.groupby('Aerolínea')['OnTime'].apply(lambda x: (x=='C').sum()).reset_index(name='count')
df_count_aerolinea = df_count_aerolinea.sort_values(by=['count'],ascending=False)
print(df_count_aerolinea)

#h) Hung Cho vuela para las Lineas Aereas 9, 4, 8 y 3
df_count_piloto = mergedDf.groupby('Aerolínea')['Piloto'].apply(lambda x: (x=='Hung Cho').sum()).reset_index(name='count')
df_count_piloto = df_count_piloto.sort_values(by=['count'],ascending=False)
print(df_count_piloto)

#i) A: 7, B: 1, C: 2
df_count_piloto_ontime = mergedDf.groupby('OnTime')['Piloto'].apply(lambda x: (x=='Chao Ma').sum()).reset_index(name='count')
df_count_piloto_ontime = df_count_piloto_ontime.sort_values(by=['count'],ascending=False)
print(df_count_piloto_ontime)
