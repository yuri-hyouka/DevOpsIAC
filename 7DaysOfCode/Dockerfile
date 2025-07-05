#Imagem Base
FROM python:3.11-alpine

#Definindo o diretório de trabalho
WORKDIR /app

#Copiando arquivos do projeto para dentro da imagem
COPY . .

#Instalando as bibliotecas listadas no requirements.txt | A Flag --no-cache-dir evita que o pip armazene o cache do download, deixando a imagem menor.     
RUN pip install --no-cache-dir -r requirements.txt

#Expõe a porta 8000 para o host
EXPOSE 8000

#Rodando o servidor de desenvolviemnto do Django.
# '0.0.0.0' permite que o servidor seja  acessível de fora do contêiner.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]