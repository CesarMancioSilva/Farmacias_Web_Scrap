import pandas as pd
def GatherFiles(all_csv_path):
    dfs = []

    for csv_path in all_csv_path:
        try:
            df = pd.read_csv(csv_path)
            dfs.append(df)
        except Exception as e:
            print(f"Erro ao ler o arquivo {csv_path}: {e}")

    if dfs:  
        df_final = pd.concat(dfs, ignore_index=True)
        
        output_path = "dados_consolidados.csv"
        df_final.to_csv(output_path, index=False)
        print(f"✅ Todos os CSVs foram unidos em: {output_path}")
    else:
        print("❌ Nenhum CSV válido foi encontrado para unir.")