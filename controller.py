# -*- coding: utf-8 -*-


# load the model
from keras.models import load_model
import numpy as np
from matplotlib import pyplot as plt
import base64
from io import BytesIO
from PIL import Image

img_rows, img_cols = 28, 28

model = load_model("model.h5")


def main(im_b64: str):
    
    try:
        im = set_image(im_b64)
        result = classify(im)
        
        return result
    except Exception as e:
        print("Exception:", e)
        return str(e)
    



def set_image(im_b64: str):
    print("llegando a set_image")
    # Decodificar base64 y abrir con PIL
    img_data = base64.b64decode(im_b64)
    img = Image.open(BytesIO(img_data)).convert("RGB")

    # Redimensionar a tamaño esperado
    img = img.resize((img_cols, img_rows))

    # Convertir a array NumPy
    im_array = np.array(img)

    gray = np.dot(im_array[...,:3], [0.299, 0.587, 0.114])
    plt.imshow(gray, cmap = plt.get_cmap('gray'))
    plt.show()
    
    # reshape the image
    gray = gray.reshape(1, img_rows, img_cols, 1)
    
    # normalize image
    gray /= 255
    
    print("imagen lista")
    return gray;



def classify(im):
    prediction = model.predict(im)
    
    print("prediction", prediction)
    
    y_hat = np.argmax(prediction)
    print("El hat:", y_hat)
    
    return y_hat


