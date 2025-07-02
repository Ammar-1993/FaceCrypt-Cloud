from utils import face_utils

# استبدل هذه المسارات بصورك المحلية لاختبار حقيقي
IMAGE_PATH_1 = "test_images/user1.jpg"
IMAGE_PATH_2 = "test_images/user2.jpg"

def load_image_from_path(path):
    from PIL import Image
    import numpy as np
    image = Image.open(path).convert('RGB')
    image = image.resize((500, 500))  # Optional: يضمن حجم معقول
    return np.asarray(image, dtype=np.uint8)



# 1️⃣ تحميل الصورتين
img1 = load_image_from_path(IMAGE_PATH_1)
img2 = load_image_from_path(IMAGE_PATH_2)

# 2️⃣ استخراج Face Encoding
encoding1 = face_utils.extract_face_encoding(img1)
encoding2 = face_utils.extract_face_encoding(img2)

print("✅ Encoding 1:", encoding1)
print("✅ Encoding 2:", encoding2)

# 3️⃣ مقارنة
result = face_utils.compare_encodings(encoding1, encoding2)
print("✅ Match Result:", result)
