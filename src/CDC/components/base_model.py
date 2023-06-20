from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import CategoricalCrossentropy
from CDC.entity.config_entity import BaseModelConfig
from pathlib import Path


class BaseModel:
    def __init__(self, config : BaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = VGG16(
            weights= self.config.params_weights,
            include_top= self.config.params_include_top,
            input_shape=self.config.params_image_size
        )

        self.model.save(self.config.base_model_path)

    
    def _prepare_full_model(self, model,classes,learning_rate,freeze_all = True,freeze_till = None):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif freeze_till:
            for layer in model.layers[:freeze_till]:
                layer.trainable = False

        flatten = Flatten()(model.output)
        predictions = Dense(classes, activation='softmax')(flatten)
        model = Model(inputs=model.input, outputs=predictions)
        model.compile(optimizer=SGD(lr=learning_rate), 
            loss=CategoricalCrossentropy(), 
            metrics=['accuracy'])
        
        return model
        
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            self.model,
            self.config.params_classes,
            self.config.params_learning_rate,
            True,
            None
        )

        self.full_model.save(self.config.updated_base_model_path)
        


    