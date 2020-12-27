import tensorflow as tf
import cv2
import numpy
import ctypes


def decode_image(img):
    # img = tf.image.decode_jpeg(img, channels=3)
    img = tf.data.Dataset.from_tensors(tf.image.resize(img, (224, 224)))
    img = img.batch(1)
    return img


model = tf.keras.models.load_model("C:\\Users\\saish\\Downloads\\model1_effnetb2_trial1.h5")
cap = cv2.VideoCapture(0)
b = 0
while True:
    ret, test_image = cap.read()
    cv2.imshow("LazEye", cv2.resize(test_image, (1000, 700)))
    # print(numpy.array(test_image).shape)
    a = model.predict(decode_image(test_image))
    if cv2.waitKey(10) == ord('b'):
        break
    if a[0][0] > 0.000001:
        print(1)  # For face
        b = 2
    else:
        print(0)  # For hand
        b += 1
    if b > 15:
        ctypes.windll.user32.LockWorkStation()
        break
cap.release()
cv2.destroyAllWindows()
