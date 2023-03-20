import keras 
from models import model_path
# from utils import read_dictionary
from keras.utils import load_img , img_to_array 
import numpy as np
import os 

shape_img = (None,None,None)
# list_of_character = read_dictionary()

class Prediction_model:
    def __init__(self):
        try:
            if  hasattr(self,'ocr_model'):
                print('Model already load')
            else:
                print('Loading Model ...')
                self.load_model()
        except:
            self.load_model()
    def load_model(self):
        self.ocr_model = keras.models.load_model(model_path)

    def predict_model(self):
        data = load_img(os.getcwd()+'/static/result.png',target_size=(28,28,1),grayscale=True)
        data = img_to_array(data)
        data = np.expand_dims(data, axis=0)
        # data = data.astype('float32') / 255.0
        predictions = self.ocr_model.predict(data)
        classes = np.argmax(predictions, axis = 1)
        return classes[0]