# Imagen base de Python
FROM python:3.11

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Instalar requerimientos
RUN pip install -r requirements.txt

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar FastAPI
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
