Leia o arquivo documentation.pdf

Crie um ambinte de desenvolvimento
- python -m venv meuAmbiente

Ative o ambiente no Windows
- .\meuAmbiente\Scripts\activate

Atualize seu pip install
- python -m pip install --upgrade pip

Instale as dependencias no arquivo requeriments.txt
- pip install -r requeriments.txt

Se houver error na etapa de instalar as dependências, vá até o Editor de registro do seu Windows 
Procure por: HKEY_LOCAL_MACHINES/SYSTEM/CurrentControlSet/Control/FileSystem
edite esse arquivo para o valor 1. Reinicie o seu computador

Crie um arquivo .env com as credenciais:

sharepoint_tenant_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" (Id do diretório - locatário)
sharepoint_client_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" (Id do aplicativo - clinte)
sharepoint_client_secret_value = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" (Valor do secret criado - Value)
