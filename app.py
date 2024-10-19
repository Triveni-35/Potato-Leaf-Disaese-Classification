from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('model.h5')
class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
BATCH_SIZE = 32
IMAGE_SIZE = 255
CHANNEL = 3
EPOCHS = 20

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'files' not in request.files:
            return render_template('index.html', message='No file part')

        files = request.files.getlist('files')  # Use 'files' instead of 'file'

        if len(files) == 0 or files[0].filename == '':
            return render_template('index.html', message='No selected file')

        results = []

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join('static', filename)
                file.save(filepath)

                # Read the image
                img = tf.keras.preprocessing.image.load_img(filepath, target_size=(IMAGE_SIZE, IMAGE_SIZE))

                # Predict using the loaded model
                predicted_class, confidence = predict(img)

                # Append result
                results.append({
                    'image_path': filepath,
                    'predicted_class': predicted_class,
                    'confidence': confidence
                })

        # Render the template with results
        return render_template('index.html', results=results)

    return render_template('index.html', message='Upload images')

# Function to preprocess and predict
def predict(img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

if __name__ == '__main__':
    app.run(debug=True)
