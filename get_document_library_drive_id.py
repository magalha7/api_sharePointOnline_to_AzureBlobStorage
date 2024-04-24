import sys
from api import auth
import requests
import json

def search(json_data, library_name):
    # Converte o JSON em um dicionário Python
    data = json.loads(json_data)

    # Verifica se a chave 'value' está presente no dicionário
    if 'value' in data:
        # Itera sobre os itens na lista 'value'
        for item in data['value']:
            # Verifica se o campo 'name' do item é igual ao 'library_name'
            if item.get('name') == library_name:
                return item  # Retorna o item se encontrado

    # Retorna None se o 'library_name' não for encontrado
    return "Nao encontrado"


def get_folders(library_name,site_name):
    
    token = auth()
    print(f"Obtendo informações da Biblioteca de documentos {library_name} do site {site_name}...")
    print(f"Token de autenticação obtido!\n\n")

    headers ={
         "Authorization": f"Bearer {token}",
         "Content-Type": "application/json"
    }


    response_site = requests.get(
        url=f"https://graph.microsoft.com/v1.0/sites?search={site_name}",
        headers=headers
    )

    if response_site.status_code == 200:
        
        response_json = response_site.json()

        if 'value' in response_json:
            # Acessa o valor do campo 'id' do primeiro item na lista 'value'
            id_site = response_json['value'][0]['id']

            response_folders = requests.get(
                url=f"https://graph.microsoft.com/v1.0/sites/{id_site}/drives",
                headers=headers
            )

            if response_folders.status_code == 200:
                response_folders = json.dumps(response_folders.json())
                folder = search(response_folders,library_name)
                if(folder != 'Nao encontrado'):
                    print(f"Para a biblioteca de documentos {library_name} seu drive_id é: "+str(folder['id']))
                else:
                    print("Não encontrado, digite o nome correto!")
            else:
                print(f"Error ao obter biblioteca de documentos do site {site_name}")

    else:
        print("Erro ao obter a resposta da API")



def main():
    if len(sys.argv) < 3:
        print("Por favor, forneça o nome da biblioteca de documentos e o nome do site como argumento.")
        return
    
    library_name = sys.argv[1]
    site_name = sys.argv[2]
    get_folders(library_name,site_name)

if __name__ == "__main__":
    main()
