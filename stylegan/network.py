import tensorflow as tf
import math
import numpy as np


class Generator(tf.keras.Model):
    def __init__(self, resolution=1024):
        super(Generator, self).__init__()
        self.generator_mapping = GeneratorMapping()
        self.generator_style = GeneratorStyle(resolution)

    def call(self, inputs):
        result = self.generator_mapping(inputs)
        result = self.generator_style(result)
        return result

    def generate(self, input=None, random_seed=42):

        if input is None:
            rnd = np.random.RandomState(random_seed)
            input = rnd.randn(1, 512)

        prediction = self.predict(input)

        images = prediction.transpose([0, 2, 3, 1])
        return np.clip((images + 1) * 0.5, 0, 1)


class GeneratorStyle(tf.keras.Model):
    def __init__(self, resolution=1024):
        super(GeneratorStyle, self).__init__()
        self.resolution_log2 = int(math.log2(resolution))
        if 2 ** self.resolution_log2 != resolution:
            raise Exception("Resolution must be a power of two")


class DiscriminatorBasic(tf.keras.Model):
    def __init__(self, resolution=1024):
        super(DiscriminatorBasic, self).__init__()
        self.resolution_log2 = int(math.log2(resolution))
        if 2 ** self.resolution_log2 != resolution:
            raise Exception("Resolution must be a power of two")

