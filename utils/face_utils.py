import numpy as np
import face_recognition
from PIL import Image
from io import BytesIO

def load_image_from_request(file):
    """
    Loads an image from a Flask request file object.
    Returns a NumPy array.
    """
    image = Image.open(BytesIO(file.read()))
    return np.array(image)

def extract_face_encoding(image_array):
    """
    Extracts the face encoding from a given image (NumPy array).
    Returns the first encoding found.
    """
    encodings = face_recognition.face_encodings(image_array)
    if len(encodings) == 0:
        raise ValueError("❌ No face detected in the image.")
    return encodings[0]

def compare_encodings(known_encoding, unknown_encoding, tolerance=0.6):
    """
    Compares two face encodings.
    Returns True if they match within the given tolerance.
    """
    results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=tolerance)
    return results[0]
