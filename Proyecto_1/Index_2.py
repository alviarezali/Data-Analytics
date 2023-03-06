import pandas as pd

answer=None

data = {
    'Date': ['2022-02-21','2022-02-21','2022-02-21','2022-02-21','2022-02-21'],
    'ID_Client': ["0021","0025","0021","0027","0027"],
    'Company': ['Digitel', 'Telefonica','Digitel', 'AT&T','AT&T'],
    'Income_Dollar': [25000,12000,13500,84000,12100]
}
df = pd.DataFrame(data)

def show_stats(df,**Kwargs):
    df = df.append(pd.DataFrame(Kwargs, index=[0]), ignore_index=True)
    print('-'*22,"The date has been added!",'-'*22)
    stats_by_company = df.groupby(['Company', 'Date'])['Income_Dollar'].agg(['min', 'max', 'mean'])
    print(df)
    print("\n")
    print("-"*15,"Statistics by Company","-"*15)
    print(stats_by_company)

df['Date'] = pd.to_datetime(df['Date']) 
print("-"*15,"Current data","-"*15)
print(df)
while True:
    print("\b")
    while answer not in ('y', 'yes', 'n', 'no'):
        answer = (input("Do you want to add any data?: (y - N): ")).lower()
    
    if answer in ('y', 'yes'):
        IdClient= input("Which is the Id cliente?: ")
        company = input("Which is the name Company?: ")
        while True:
            income = int(input("Please, enter the Income ($): "))
            try:
                if income <= 0:
                    raise ValueError
                break
            except:
                print("Invalid input. Please enter a positive integer for the Income") 
        
        while True:
            date = input("Which date? (YYYY-MM-DD): ")
            try:
                date = pd.to_datetime(date)
                break
            except:
                print("Invalid format. Please enter a date in YYYY-MM-DD format") 


        # newLine = {'Date': date, 'ID_Client': IdClient, 'Company': company, 'Income_Dollar': income}
        show_stats(df, Date=date,ID_Client= IdClient, Company=company, Income_Dollar=income)
        
    else:
        print("The program has finalized. GoodBye!")
        break
    answer = None
    
