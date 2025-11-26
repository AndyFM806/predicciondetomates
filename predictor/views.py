from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from keras.saving import load_model
import numpy as np
from PIL import Image
import os

MODEL_PATH = os.path.join(settings.BASE_DIR, "model", "cnn_simple.keras")
model = load_model(MODEL_PATH)

IMG_SIZE = (224, 224)

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        file_url = fs.url(filename)
        file_path = fs.path(filename)

        # Preprocesar imagen
        img = Image.open(file_path).convert("RGB")
        img = img.resize(IMG_SIZE)
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predicción
        pred = model.predict(img_array)[0][0]
        label = "Tomate saludable" if pred < 0.5 else "Tomate no saludable"

        return render(request, "predictor/result.html", {
            "image_url": file_url,
            "prediction": label,
            "raw_score": float(pred)
        })

    return render(request, "predictor/upload.html")
