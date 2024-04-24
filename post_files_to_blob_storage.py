#Example: python .\post_files_to_blob_storage.py "DefaultEndpointsProtocol=https;AccountName=datalakeblobstorage01;AccountKey=uTCHu2X1wap1mDUPLEsI7fWMr2ZMYaFl9yRn3vhZKd9JZCv+XLD3v+zfbv0ss8CvalihA6F3pLQC+AStj4c6Jg==;EndpointSuffix=core.windows.net" "educacao" "/testeFile/teste/base_diretorias.xlsx" "arquivos baixados\base_diretorias.xlsx"

import sys
from api import auth
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def upload_file_in_blob(connection_string, name_container, path_in_blob, path_in_local):

    # Conectando-se ao serviço de armazenamento de blob
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    try:
        # Upload do arquivo para o Blob Storage
        blob_client = blob_service_client.get_blob_client(container=name_container, blob=path_in_blob)
        with open(path_in_local, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            print("Arquivo enviado com sucesso para o Azure Blob Storage!")
    except Exception as e:
        print("Ocorreu um erro:", e)



def main():
    if len(sys.argv) < 5:
        print("Por favor, forneça:")
        print("Sua connection_string \n")
        print("Nome do seu container \n")
        print("Nome do caminho onde será salvo arquivo \n")
        print("Nome do caminho onde está o arquivo \n")
        return
    connection_string = sys.argv[1]
    name_container = sys.argv[2]
    path_in_blob = sys.argv[3]
    path_in_local = sys.argv[4]

    upload_file_in_blob(connection_string, name_container, path_in_blob, path_in_local)

if __name__ == "__main__":
    main()
