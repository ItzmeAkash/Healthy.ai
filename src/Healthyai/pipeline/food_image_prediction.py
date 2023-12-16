import numpy as np
import tensorflow as tf

import keras
from keras.preprocessing import image
from keras.models import load_model
import os
from Healthyai.utils.common import read_labels_from_file

class FoodImagePredictionPipeline:
    def __init__(self,filename):
        self.filename = filename
        
        
    def predict(self):
        #load_model
        model = load_model(os.path.join("artifacts","food_image_classification","training","model.h5"))
        
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image) ,axis=1)
        print(result)
        
        
        label = {0:'apple_pie',1: 'cheesecake', 2:'chicken_curry',3: 'french_fries',4: 'fried_rice',5: 'hamburger', 6:'hot_dog', 7:'ice_cream', 8:'omelette',9: 'pizza',10: 'sushi'}
        for i in label:
         if result[0]==i:
           predicion = label[i]
           print(predicion)
           return [{"image":predicion}]
        return "Not"
        