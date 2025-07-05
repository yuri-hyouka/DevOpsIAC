#Imagem Base
FROM python:3.9-slim

#Definindo o diretório de trabalho
WORKDIR /app

#Copiando arquivos do projeto para dentro da imagem
COPY . .

#Instalando as bibliotecas listadas no requirements.txt | A Flag --no-cache-dir evita que o pip armazene o cache do download, deixando a imagem menor.     
RUN pip install --no-cache-dir -r requirements.txt

#Rodando o projeto
CMD ["python", "main.py"]