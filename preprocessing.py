import pandas as pd

file = "Solicitações SIC - Volumetria de Refeições.xlsx"
sheets = pd.ExcelFile(file).sheet_names
print("Sheets encontrados:", sheets)

dfs = []
for sh in sheets:
    try:
        df_temp = pd.read_excel(file, sheet_name=sh, header=1)
        if df_temp.empty:
            print(f"Sheet '{sh}' está vazio, ignorando.")
            continue
        if dfs:
            colunas_comuns = set(df_temp.columns).intersection(set(dfs[0].columns))
            if not colunas_comuns:
                print(f"Sheet '{sh}' não possui colunas em comum, ignorando.")
                continue
        dfs.append(df_temp)
        print(f"Sheet '{sh}' adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao ler sheet '{sh}': {e}")

# Concatenar todos os sheets válidos, alinhando pelo nome da coluna
if dfs:
    df_vol_meal = pd.concat(dfs, ignore_index=True, sort=False)
    print("\nDataFrame final:")
    print(df_vol_meal.head())
else:
    print("Nenhum sheet válido para concatenar.")

# df_vol_meal = pd.read_excel('Solicitações SIC - Volumetria de Refeições.xlsx')
# df_vol_meal = df_vol_meal.drop(0)
# df_vol_meal = df_vol_meal.rename(columns={'Unnamed: 0': 'date', 'ALMOÇO': 'almoco_ru', 'Unnamed: 2': 'almoco_ra', 'Unnamed: 3': 'almoco_rs',
#                            'Unnamed: 4': 'total_almoco', 'JANTAR': 'jantar_ru', 'Unnamed: 7': 'jantar_ra', 'Unnamed: 8': 'jantar_rs',
#                            'Unnamed: 9': 'total_jantar'})
# df_vol_meal['date'] = pd.to_datetime(df_vol_meal['date'], format='%Y/%m/%d')

# print(df_vol_meal)
# ALTERAÇÕES A SEREM FEITAS DEPOIS DA REUNIÃO
# Espcificar as colunas de interesse em cada sheet e fazer o procedimento de concatenação
# Tratar os valores nulos
# Tratar os valores que estão como texto (verficar se todos os nomes de refeições estão corretos, sem espaços, etc)
# Organizar as colunas (ex: almoçço_ru, almoco_ra, almoco_rs, total_almoco, jantar_ru, jantar_ra, jantar_rs, total_jantar)
