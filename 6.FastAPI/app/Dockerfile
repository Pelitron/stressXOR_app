FROM python:3.11-slim

# Eliminar configuraciones previas de fuentes y establecer una nueva
RUN rm -f /etc/apt/sources.list /etc/apt/sources.list.d/* \
    && echo "deb [trusted=yes] http://deb.debian.org/debian bookworm main" > /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y libgl1-mesa-glx \
    && rm -rf /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin
    
# Establecer directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto (Cloud Run usa 8080 por defecto)
EXPOSE 8080

# Comando para ejecutar la aplicación con Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]