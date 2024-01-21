import pandas as pd
from PIL import Image
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os
import numpy as np

def load_image(file_path):
    return Image.open(file_path)

def load_dataset(data_path, label):
    image_list = []
    label_list = []

    for root, dirs, files in os.walk(os.path.join(data_path, label)):
        for file in files:
            if file.endswith(".jpg"):
                file_path = os.path.join(root, file)
                image = load_image(file_path)
                image_list.append(image)
                label_list.append(label)

    return image_list, label_list


def count_images_in_subfolders(dataset_path):
    class_counts = {}
    
    for class_name in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_path):
            images = [file for file in os.listdir(class_path) if file.endswith('.jpg')]
            class_counts[class_name] = len(images)
    
    return class_counts


def preprocess_data(df):
    # Code for data preprocessing
    feature_columns = ['feature1', 'feature2', 'feature3']
    X = df[feature_columns]

    # Perform any preprocessing steps (e.g., scaling)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled

def preprocess_images(image_list, target_size=(224, 224), normalize=True):
    processed_images = [np.array(image.resize(target_size)) / 255.0 if normalize else np.array(image.resize(target_size)) for image in image_list]
    return np.array(processed_images)

# Define the target size for resizing
target_size = (224, 224)

# Load training data
train_health_images, train_health_labels = load_dataset(train_path, 'health')
train_mildew_images, train_mildew_labels = load_dataset(train_path, 'mildew')

# Load validation data
validation_health_images, validation_health_labels = load_dataset(validation_path, 'health')
validation_mildew_images, validation_mildew_labels = load_dataset(validation_path, 'mildew')

# Load test data
test_health_images, test_health_labels = load_dataset(test_path, 'health')
test_mildew_images, test_mildew_labels = load_dataset(test_path, 'mildew')

# Preprocess images for training, validation, and test sets
train_images = preprocess_images(train_health_images + train_mildew_images, target_size=target_size)
validation_images = preprocess_images(validation_health_images + validation_mildew_images, target_size=target_size)
test_images = preprocess_images(test_health_images + test_mildew_images, target_size=target_size)

# Convert labels to numerical format
label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_health_labels + train_mildew_labels)
validation_labels_encoded = label_encoder.transform(validation_health_labels + validation_mildew_labels)
test_labels_encoded = label_encoder.transform(test_health_labels + test_mildew_labels)

# Optionally, you can further split your training set into training and testing subsets
# X_train, X_test, y_train, y_test = train_test_split(train_images, train_labels_encoded, test_size=0.2, random_state=42)

# Further preprocessing and model training can be performed after this

