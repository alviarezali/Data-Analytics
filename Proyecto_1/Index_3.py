import pandas as pd
#import numpy as np
data = {'Mes':['Enero', 'Febrero','Marzo','Abril','Mayo'],
        'Ventas':[30500,35600,28300,33900,42500],
        'Gastos':[22000,23450,18100,35700,32450]
        }

df = pd.DataFrame(data)

df["Columna 1"]= (df["Gastos"]/df['Ventas'])*100
# df['Columna 2'] = np.where(df["Ventas"]>=30000, "Metas Superada", "Meta No Superada")
df["Columna 2"] = ["Meta Superada" if v >= 30000 else "Meta No Superada" for v in df["Ventas"]]
df["Columna 3"] = [x-v if x>v else 0 for x,v in zip(df["Gastos"], df["Ventas"])]
print(f"El total de ventas de los últimos 3 meses es {df.tail(3)['Ventas'].sum()}")
print(f"El total de gastos de Febrero a Abril es {df.iloc[1:3,df.columns.to_list().index('Gastos')].sum()}")


