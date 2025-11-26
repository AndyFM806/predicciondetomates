import json
import tensorflow as tf
from keras import models

# RUTAS
CONFIG_PATH = "model/config.json"
WEIGHTS_PATH = "model/model.weights.h5"
OUTPUT_MODEL = "model/cnn_simple.keras"

# 1. Leer config.json
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

# 2. Extraer la arquitectura
model_config = config["config"]   # <-- AQUÍ ESTABA EL PROBLEMA

# 3. Reconstruir el modelo desde config
print("Reconstruyendo modelo...")
model = models.Model.from_config(model_config)

# 4. Cargar pesos
print("Cargando pesos...")
model.load_weights(WEIGHTS_PATH)

# 5. Guardar como modelo Keras v3
print("Guardando modelo en formato .keras...")
model.save(OUTPUT_MODEL)

print("✔ Conversión completada. Archivo creado:")
print(OUTPUT_MODEL)
