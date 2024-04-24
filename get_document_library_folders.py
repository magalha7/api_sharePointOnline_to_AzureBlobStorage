import sys
from api import auth
import requests
import json


def get_folders(doc_library_id,item_path):

    token = auth()
    print(f"Obtendo informações do ID pasta: {doc_library_id} da pasta {item_path}")
    print(f"Token de autenticação obtido!\n\n")

    headers ={
         "Authorization": f"Bearer {token}",
         "Content-Type": "application/json"
    }

    response = requests.get(
        url=f"https://graph.microsoft.com/v1.0/drives/{doc_library_id}/root:/{item_path}:/children",
        headers=headers
    )

    if response.status_code == 200:
            response = json.dumps(response.json())
            print(response)
    else:
        print('Error ao obter resposta da API, verifique os parametros!')


def main():

    if len(sys.argv) < 3:
        print("Por favor, forneça o id do site e o caminho da Biblioteca de documentos")
        return
    
    doc_library_id = sys.argv[1]
    item_path = sys.argv[2]
    get_folders(doc_library_id, item_path)

if __name__ == "__main__":
    main()
