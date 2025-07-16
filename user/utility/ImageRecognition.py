from imageai.Prediction import ImagePrediction
import os
from django.conf import settings


class Recognitions:
    def start_process(self, filepath):
        execution_path = os.getcwd()
        prediction = ImagePrediction()
        prediction.setModelTypeAsResNet()
        dataset = settings.MEDIA_ROOT + "\\" + 'resnet50_weights_tf_dim_ordering_tf_kernels.h5'
        filepath = settings.MEDIA_ROOT + "\\" + filepath
        print("Path is " + dataset)
        print("Execution path :" + execution_path)
        prediction.setModelPath(dataset)
        prediction.loadModel()
        resultDict = {}
        predictions, percentage_probabilities = prediction.predictImage(filepath, result_count=100)
        for index in range(5):
            print(predictions[index], " : ", percentage_probabilities[index])
            resultDict.update({predictions[index]: round(percentage_probabilities[index], 2)})

        return resultDict;
