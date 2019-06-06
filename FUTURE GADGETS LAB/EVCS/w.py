import warnings
import pathlib
warnings.filterwarnings(action="ignore", message="^internal gelsd")


from imageai.Detection import ObjectDetection
import os
import pickle
import numpy as np
model = pickle.load(open('modelGud.pkl', 'rb'))
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath('./yolo-tiny.h5')
detector.loadModel()
custom = detector.CustomObjects(car = True)
path = "./electricStations"
evList = []
for i in os.listdir(path):
    if i.endswith('jpg'):
        evList.append(i)

def customPrice(electricStation):
    evPath = './electricStations/' + electricStation
    detections = detector.detectCustomObjectsFromImage(custom_objects=custom , input_image = evPath ,output_image_path = './output/' + electricStation + '.jpg', minimum_percentage_probability=30)
    numberOfCars = 0
    for car in detections:
        numberOfCars += 1
    #print(numberOfCars)
    time = np.random.randint(1,13)
    dayNight = np.random.randint(0,2)
    chargingPoints = 6
    waitingTime = round((numberOfCars * (1/3))*(1/chargingPoints) , 2)
    return(waitingTime)

class priceTime():
    @property
    def results(self):
        priceTime = []
        for j in evList:
            time = customPrice(j)
            #print(price , time)
            priceTime.append([time])
        print(priceTime)
        
        

    
