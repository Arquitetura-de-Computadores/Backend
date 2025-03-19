FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Flask usará
EXPOSE 5050

# Comando para rodar o backend
CMD ["python", "app.py"]
