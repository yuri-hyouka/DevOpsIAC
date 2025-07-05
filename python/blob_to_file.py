import mysql.connector
import os

# Configurações do banco de dados
config = {
    'host': 'ip_adress',
    'user': 'user',
    'password': 'senha',
    'database': 'bd'
}

# Caminho onde os arquivos serão salvos
diretorio_destino = '/home/yuri/arquivos'
os.makedirs(diretorio_destino, exist_ok=True)

# Conexão com o banco
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

#cursor.execute("SELECT id, nome_arquivo, arquivo_blob FROM documentos")
cursor.execute("select id as doc_id, chamado_id, arquivo as arquivo_blob, nome as nome_arquivo from anexo where chamado_id < 56714")


for doc_id, chamado_id, arquivo_blob, nome_arquivo,  in cursor:
    caminho_diretorio = os.path.join(diretorio_destino, str(chamado_id))
    caminho_arquivo   = os.path.join(diretorio_destino, str(chamado_id), nome_arquivo)
    os.makedirs(caminho_diretorio, exist_ok=True)
    with open(caminho_arquivo, 'wb') as f:
        f.write(arquivo_blob)
    print(f'Arquivo {nome_arquivo} (ID: {doc_id}) salvo com sucesso em {caminho_arquivo}')

# Limpeza
cursor.close()
conn.close()