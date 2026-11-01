import sys
import tensorflow as tf
from keras.applications import MobileNetV2
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.mobilenet_v2 import preprocess_input

Dog_class = range(151,269)
Cat_class = range(281,286)

model = MobileNetV2(weights="imagenet")

def main(path) :

    img = tf.image.decode_image(tf.io.read_file(path),channels=3)
    img = tf.image.resize(img,(224,224))

    x = tf.expand_dims(preprocess_input(img),0)
    pred = model.predict(x,verbose = 0)
    name = decode_predictions(pred,top=1)[0][0][1]
    idx = pred.argmax()

    if idx in Dog_class :
        label = "Dog"
        
    elif idx in Cat_class :
        label = "Cat"
    else:
        label = "Other"

    print(f"{name}:{label}")


if __name__=="__main__":
    main(sys.argv[1])
