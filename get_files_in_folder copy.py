import sys
from api import auth
import requests
import json
import wget
import pandas as pd


def download_files(df,file_name):

    df.to_excel(file_name, index=False)

def get_file(item_id,drive_id):


    token = auth()
    headers ={
         "Authorization": f"Bearer {token}",
         "Content-Type": "application/json"
    }

    response = requests.get(
            url=f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{item_id}",
            headers=headers
    )

    if(response.status_code == 200):

        resposta_json = response.text
        dados = json.loads(resposta_json)
        wget.download(dados['@microsoft.graph.downloadUrl'],'arquivos baixados')    

    else:
        print("Error ao obter dados da API")




def get_files_in_folder(drive_id,relative_path):
    
    token = auth()
    print(f"Obtendo informações...")
    print(f"Token de autenticação obtido!\n\n")

    headers ={
         "Authorization": f"Bearer {token}",
         "Content-Type": "application/json"
    }


    response = requests.get(
        url=f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root:/{relative_path}:/children",
        headers=headers
    )

    print(response.content)

    if response.status_code == 200:
        
            response_json = response.json()['value']
            df = pd.DataFrame(response_json)
            if(not (df.empty)):
                for index, row in df.iterrows():
                    item_id = row['id']
                    file_name = row['name']
                    get_file(item_id,drive_id)
                    # download_files(df,file_name)
       
    else:
        print("Erro ao obter a resposta da API")



def main():
    if len(sys.argv) < 3:
        print("Por favor, forneça o id da biblioteca de documentos e o caminho da pasta/subpasta que contém os arquivos.")
        return
    
    drive_id = sys.argv[1]
    relative_path = sys.argv[2]
    get_files_in_folder(drive_id,relative_path)

if __name__ == "__main__":
    main()
