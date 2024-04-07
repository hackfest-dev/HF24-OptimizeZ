import tensorflow as tf
import os
import numpy as np
from skimage.io import imread, imshow
from skimage.transform import resize
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2
import matplotlib.image as mpimg
from keras.models import load_model

def geoParams(image_path):
    model = load_model('C:/Users/Muthu/Desktop/Hackfest/OptimizeZ/HF24-OptimizeZ/Server/woundSegmentation_model.h5')
    IMG_WIDTH = 128
    IMG_HEIGHT = 128
    IMG_CHANNELS = 3
    # Get the directory path of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Specify the output directory
    output_directory = os.path.join(current_directory, "output")
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    image = Image.open(image_path)

    # Resize the image to (128, 128)
    resized_image = image.resize((128, 128))

    # Convert the image to a numpy array
    resized_array = np.array(resized_image)
    
    predicted_mask = model.predict(np.expand_dims(resized_array , axis=0))
    preds_test_t = (predicted_mask > 0.5).astype(np.uint8)
    # Assuming X_test[var] and woundIsolation are your images
    woundIsolation = preds_test_t
    woundColorIsolation = resized_array * preds_test_t
    plt.figure(figsize=(15, 5))


    # Plot the second image (woundIsolation overlay)
    plt.subplot(1, 3, 2)
    plt.imshow(woundIsolation.squeeze(), cmap='gray')  # Assuming woundIsolation is grayscale
    plt.title('Wound Isolation Overlay')
    plt.axis('off')
    

    # Plot the third image (woundColorIsolation overlay)
    plt.subplot(1, 3, 3)
    plt.imshow(woundColorIsolation.squeeze(), cmap='gray')  # Assuming woundColorIsolation is grayscale
    plt.title('Wound Color Isolation Overlay')
    plt.axis('off')
    plt.savefig("wi3.png", bbox_inches='tight', pad_inches=0)
    image = cv2.imread("wi3.png")
    cv2.imwrite(os.path.join(output_directory,"2.jpg"), image)



    # Adjust layout
    plt.tight_layout()
    woundIsolation = (woundIsolation * 255).astype(np.uint8)

    # Convert to PIL Image
    Maskedimage = Image.fromarray(woundIsolation.squeeze())  # mode='L' for grayscale

    # Save the images
    Maskedimage.save("MaskedTest_output_image.png")

    # Load the saved images
    Maskedimage = cv2.imread("MaskedTest_output_image.png")
    

    gray = cv2.cvtColor(Maskedimage, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest_contour)
    perimeter = cv2.arcLength(largest_contour, True)
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.drawContours(Maskedimage, [largest_contour], -1, (0, 255, 0), 1)
    cv2.rectangle(Maskedimage, (x, y), (x + w, y + h), (255, 0, 0), 1)

    # Create a figure with subplots
    plt.figure(figsize=(16, 8))

    # Display the original image with properties
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(Maskedimage, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.text(x + w + 2, y + 3, f'Height: {h}', color='red', fontsize=10)
    plt.text(x + w + 2, y + 7, f'Width: {w}', color='red', fontsize=10)
    plt.text(x + w + 2, y + 11, f'Area: {area}', color='red', fontsize=10)
    plt.text(x + w + 2, y + 15, f'Perimeter: {perimeter:.2f}', color='red', fontsize=10)
    plt.savefig("pr_image.png", bbox_inches='tight', pad_inches=0)
    image = cv2.imread("pr_image.png")
    cv2.imwrite(os.path.join(output_directory,"3.jpg"), image)
    
    return h, w, area, perimeter



