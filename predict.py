from PIL import Image
from io import BytesIO
import numpy as np
from keras.models import load_model


class Prediction:
    def __init__(self):
        self.image_size = (240, 240)

        self.efficient_net_B2_model = load_model("./effB1.h5")
        self.classes = np.array(
            ["Bacterial Spot", "Early Blight", "Healthy", "Late Blight", "Leaf Mold", "Mosaic Virus", "Septoria Leaf Spot", "Target Spot", "Spider Mite", "Yellow Leaf Curl Virus"])

    def read_image(self, image_encoded):
        pil_image = Image.open(BytesIO(image_encoded))
        return pil_image

    def preprocess(self, image: Image.Image):
        resized_image = image.resize(self.image_size)
        resized_image = np.asfarray(resized_image)
        # resized_image = resized_image / 255.
        resized_image = np.expand_dims(resized_image, 0)
        return resized_image

    def predict(self, image):
        effb2_prediction = self.classes[np.argmax(
            self.efficient_net_B2_model.predict(image), axis=1)][0]

        return effb2_prediction
