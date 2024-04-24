import sys
from api import auth
import requests
import json

def get_list_info(name_list,site_id):
    token = auth()
    print(f"Obtendo informações da lista {name_list}...")
    print(f"Token de autenticação obtido!\n\n")

    headers ={
         "Authorization": f"Bearer {token}",
         "Content-Type": "application/json"
    }

    response = requests.get(
          url=f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{name_list}",
          headers=headers
    )

    if response.status_code == 200: 

        response_final = json.dumps(response.json())
        print("Resposta: \n")
        print(response_final)
    
    else:
        print("Erro ao obter a resposta da API")


def main():
    if len(sys.argv) < 3:
        print("Por favor, forneça o nome da lista e o ID do site como argumentos.")
        return
    
    name_list = sys.argv[1]
    site_id = sys.argv[2]
    get_list_info(name_list,site_id)

if __name__ == "__main__":
    main()
