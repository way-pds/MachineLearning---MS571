import pandas as pd

file = 'Solicitações SIC - Volumetria de Refeições.xlsx'
sheets = pd.ExcelFile(file).sheet_names
print("Sheets encontrados:", sheets)

# Lê e concatena todos
df_vol_meal = pd.concat(
    [pd.read_excel(file, sheet_name=sh).assign(mes=sh) for sh in sheets],
    ignore_index=True
) 

#df_vol_meal = pd.read_excel('Solicitações SIC - Volumetria de Refeições.xlsx')
df_vol_meal = df_vol_meal.drop(0)
df_vol_meal = df_vol_meal.rename(columns={'Unnamed: 0': 'date', 'ALMOÇO': 'almoco_ru', 'Unnamed: 2': 'almoco_ra', 'Unnamed: 3': 'almoco_rs', 
                            'Unnamed: 4': 'total_almoco', 'JANTAR': 'jantar_ru', 'Unnamed: 7': 'jantar_ra', 'Unnamed: 8': 'jantar_rs',
                            'Unnamed: 9': 'total_jantar'})
#df_vol_meal['date'] = pd.to_datetime(df_vol_meal['date'], format='%Y/%m/%d')

print(df_vol_meal)
