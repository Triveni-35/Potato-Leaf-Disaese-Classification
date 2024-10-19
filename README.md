<img width="902" alt="image" src="https://github.com/user-attachments/assets/c5e53e35-47f9-42b0-b128-e4c45b5202a6">
<br>
<img width="892" alt="image" src="https://github.com/user-attachments/assets/93d6625e-6008-422c-ba55-4f0157b9e8ff">
<br>
<img width="679" alt="image" src="https://github.com/user-attachments/assets/bcf228d1-7625-4a8c-8328-f0b20e4704fc">
<br>
<img width="452" alt="image" src="https://github.com/user-attachments/assets/9568508c-efd7-452d-b5ce-e21c6863b978">
<br>
<img width="127" alt="image" src="https://github.com/user-attachments/assets/6af4553e-0db8-415f-8734-3ffc3ece9602">
<br>
Requirements
Python: Version 3.10 or higher
Flask: For creating the web application
TensorFlow
Keras: For model architecture and preprocessing images
NumPy: For numerical operations
Werkzeug: For secure filename handling
Pandas: For data manipulation and analysis
Matplotlib: For visualizing results and model performance
Bootstrap: For styling the frontend of the web application
HTML/CSS: For creating the user interface<br>
Hardware Requirements
Computer: A machine with enough RAM and CPU power to handle image processing and model inference
Dataset:
PlantVillage Dataset: A dataset containing images of potato leaves, classified into categories like 'Potato Early Blight', 'Potato Late Blight', and 'Potato Healthy'.<br>
Brief Project Description
This project aims to create a web application for the classification of potato diseases using a deep learning model. The following steps occur during the project:

Data Collection and Preparation:

A dataset containing images of potato leaves is collected (e.g., from the PlantVillage dataset).
Images are preprocessed, which may include resizing, normalization, and data augmentation to improve model performance.
Model Training:

A Convolutional Neural Network (CNN) is built and trained on the dataset to recognize different diseases affecting potato plants.
The model learns to classify images into three categories: Early Blight, Late Blight, and Healthy.
Model Saving:

Once trained, the model is saved in the .h5 format, allowing it to be loaded and used for predictions in the web application.
Web Application Development:

A Flask web application is created, featuring an intuitive user interface that allows users to upload images of potato leaves for classification.
Upon submission, the uploaded images are processed by the trained model, which predicts the disease and provides confidence levels for the predictions.
User Interaction:

Users can upload multiple images at once, and the application will display the predicted label and confidence for each image in a visually appealing format.
The application handles errors gracefully, informing users if there are issues with the uploaded files.
Results Presentation:

The results are presented in a clear, styled manner, showcasing the input images along with the corresponding predictions and confidence levels, enhancing user experience.
Conclusion
The project combines deep learning and web development to create a useful tool for farmers and agricultural experts, enabling them to quickly identify diseases affecting potato crops. The use of Flask allows for easy deployment, and the integration of TensorFlow facilitates the use of advanced machine learning techniques.
