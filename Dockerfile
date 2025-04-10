# Imagen base de Python 3.11 (puedes ajustarlo a la versión que necesites)
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt /app/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY . /app

# Exponer el puerto en el que correrá la API
EXPOSE 8000

# Comando para ejecutar la API con Uvicorn (puedes ajustar el nombre del archivo principal de tu API)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
