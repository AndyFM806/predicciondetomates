# Imagen base de Python
FROM python:3.10-slim

# Para evitar preguntas en instalaciones
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias de Python (incluye TensorFlow)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar proyecto entero
COPY . .

# Exponer puerto
ENV PORT=8000

# Comando para ejecutar Django con Gunicorn
CMD ["gunicorn", "tomato_quality.wsgi:application", "--bind", "0.0.0.0:8000"]
