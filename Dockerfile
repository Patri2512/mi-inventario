# 1. Traemos una "computadora" que ya tiene Python instalado
FROM python:3.10-slim

# 2. Creamos una carpeta dentro de esa computadora para nuestro código
WORKDIR /app

# 3. Copiamos la "lista de compras" e instalamos Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos todo el contenido de tu carpeta actual (app.py, templates, etc.)
COPY . .

# 5. Avisamos que el servidor usará el puerto 5000
EXPOSE 5000

# 6. El comando que "enciende" el servidor automáticamente al iniciar
CMD ["python", "app.py"]