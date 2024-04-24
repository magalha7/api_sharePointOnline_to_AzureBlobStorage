import sys
from api import auth
import requests
import json

def get_site_info(name_site):
    token = auth()
    print(f"Obtendo informações do site {name_site}...")
    print(f"Token de autenticação obtido!\n\n")

    headers ={
         "Authorization": f"Bearer {token}",
         "Content-Type": "application/json"
    }

    response = requests.get(
          url=f"https://graph.microsoft.com/v1.0/sites?search={name_site}",
          headers=headers
    )

    if response.status_code ==  200:
        response_final = json.dumps(response.json())
        print("Resposta: \n")
        print(response_final)
    else:
        print("Erro ao obter a resposta da API")


def main():
    if len(sys.argv) < 2:
        print("Por favor, forneça o nome do site como argumento.")
        return
    name_site = sys.argv[1]
    get_site_info(name_site)

if __name__ == "__main__":
    main()
