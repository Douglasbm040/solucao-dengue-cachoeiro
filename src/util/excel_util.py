import pandas as pd
import os
def save_to_excel(dataset, output_dir, filepath):
    df = pd.DataFrame(dataset)
    
    os.makedirs(output_dir, exist_ok=True)  
    filename = os.path.splitext(os.path.basename(filepath))[0]
    output_filepath = os.path.join(output_dir, filename + '.xlsx')

    df.to_excel(output_filepath, index=False)
    print(f"Dados foram salvos no arquivo '{output_filepath}'")