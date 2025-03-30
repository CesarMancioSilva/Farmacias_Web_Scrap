import csv
from scripts.products import extract_product_data

def transform_save_csv(csv_path,items,category,farmacia_name):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                    if items:
                        extracted_data = [extract_product_data(item,farmacia_name) for item in items]
                        
                        fieldnames = extracted_data[0].keys()
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        
                        writer.writeheader()
                        writer.writerows(extracted_data)
                        
                        print(f"Dados salvos em CSV: {csv_path}")
                        print(f"Total de itens processados: {len(extracted_data)}")
                        return csv_path
                    else:
                        print(f"Nenhum item encontrado para a categoria {category}")