import pandas as pd
import numpy as np

discount = 5
answer = ""

def percent(value, x = 5):
    result = value*(100-x)/100
    return result

df = pd.DataFrame([
    ['Televisor',50,100],
    ['Video Beam', 20, 85],
    ['Reloj Casio', 35, 130],
    ['Monitor 144Hz', 25, 250 ],
    ['Teclado Mecanico', 30, 35]
    ], columns=['Producto', 'N° Unidades','Precio Unitario ($)'],
    index= pd.date_range('20220711',periods=5, freq='D' ))

df[f"Discount {discount}%"] = (df['Precio Unitario ($)'].apply(lambda i: percent(i, x=discount)))
print("-"*30,"Current data","-"*30)
print(df)

while True:
    print("\b")
    while answer not in ('y', 'yes', 'n', 'no'):
        answer = (input("Do you want to add any data?: (y - N): ")).lower()


    if answer in ('y', 'yes'):
        product = input('Add one product: ')
        while True:
            Nunits = input('Add numbers of products: ')
            try:
                Nunits = int(Nunits)
                if Nunits <= 0:
                    raise ValueError
                break
            except ValueError:
                print('Invalid input. Please enter a positive integer for the number of units.')
        while True:
            price = input("Which is the price per unit?: ")
            try:
                price = float(price)
                if price <= 0:
                    raise ValueError
                break
            except ValueError:
                print('Invalid input. Please enter a positive number for the price per unit.')
                
        while True:
            date = input("Which date? (YYYY-MM-DD): ")
            try:
                date = pd.to_datetime(date)
                break
            except:
                print("Invalid format. Please enter a date in YYYY-MM-DD format")
                
                
        df.loc[date] = [product, Nunits, price, percent(value=price)]
        print('-'*22,"The product has been added!",'-'*22)
        print(df.tail())
        
    else:
        print("The program has finalized. GoodBye!")
        break
    
    answer = ""