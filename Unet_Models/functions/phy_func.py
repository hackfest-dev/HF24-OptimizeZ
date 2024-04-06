from roboflow import Roboflow
import supervision as sv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def phyParams(image_path):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_directory = os.path.join(current_directory, "output")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    rf = Roboflow(api_key="oGGjBy2IYnpw8cLjc6ba")
    project = rf.workspace().project("tissues-v3b6t")
    model = project.version(1).model
    result = model.predict(image_path, confidence=40).json()

    labels = [item["class"] for item in result["predictions"]]

    detections = sv.Detections.from_roboflow(result)

    label_annotator = sv.LabelAnnotator()
    mask_annotator = sv.MaskAnnotator()

    image = cv2.imread(image_path)

    annotated_image = mask_annotator.annotate(scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections, labels=labels)

    # sv.plot_image(image=annotated_image, size=(16, 16))
    cv2.imwrite(os.path.join(output_directory,"annotated_image.png"), annotated_image)
    
    return labels[0]
    
    
    
#phyParams("Unet_Models/functions/leg1.jpg")