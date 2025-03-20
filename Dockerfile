# Usa a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /backend

# Copia todos os arquivos da pasta backend para dentro do container
COPY . /backend

# Instala as dependências
RUN pip install --no-cache-dir -r /backend/requirements.txt

# Expõe a porta usada pelo Flask
EXPOSE 5050

# Comando para rodar o backend
CMD ["python", "App.py"]
