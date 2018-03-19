import tensorflow as tf
import numpy as np
import os
# import cv2
# import matplotlib.image as mpimg
from PIL import Image
from PIL import ImageFilter
import scipy.misc


def main(unused_arg):
    gaussian_blur = 2
    path = "./datasets/VOC_2007/traindata/VOC2007/JPEGImages/"
    path_to_image_names = "./datasets/VOC_2007/traindata/VOC2007/ImageSets/Main/aeroplane_train.txt"
    # image_names = os.listdir(path)
    image_names = open(path_to_image_names).readlines()

    amount_of_train_images = len(image_names)

    padded_images = np.zeros(shape=(amount_of_train_images, 500, 500, 3))
    blurred_padded_images = np.zeros(shape=(amount_of_train_images, 500, 500, 3))
    sess = tf.InteractiveSession()
    # for i in range(len(image_names)):
    print("Starting padding/blurring images..")
    for i in range(amount_of_train_images):
        print(i)
        # Get image
        filename = image_names[i].split(' ')[0] + '.jpg'
        image_loc = path + "/" + filename
        # image = mpimg.imread(image_loc)
        image = Image.open(image_loc)

        # Pad image
        t = tf.image.resize_image_with_crop_or_pad(image, 500, 500)
        padded = t.eval()

        # Convert from numpy to PIL image
        pil_padded_image = Image.fromarray(padded)

        # Blur image
        blurred = pil_padded_image.filter(ImageFilter.GaussianBlur(gaussian_blur))

        # Store in respective arrays to be saved
        padded_images[i] = padded
        blurred_padded_images[i] = blurred

    print("Saving padded/blurred..")
    np.save('./VOC_data/voc07_train_only_padded.npy', padded_images)
    np.save('./VOC_data/voc07_train_only_blurred_padded.npy', blurred_padded_images)

    padded_images = None
    blurred_padded_images = None

    cropped_images = np.zeros(shape=(amount_of_train_images, 227, 227, 3))
    blurred_cropped_images = np.zeros(shape=(amount_of_train_images, 227, 227, 3))

    image_names = open(path_to_image_names).readlines()

    sess = tf.InteractiveSession()
    # for i in range(len(image_names)):
    print("Starting cropping/blurring images..")
    for i in range(amount_of_train_images):
        print(i)
        # Get image
        filename = image_names[i].split(' ')[0] + '.jpg'
        image_loc = path + "/" + filename
        # image = mpimg.imread(image_loc)
        image = Image.open(image_loc)

        # crop image
        t = tf.image.resize_image_with_crop_or_pad(image, 227, 227)
        cropped = t.eval()

        # Convert from numpy to PIL image
        pil_cropped_image = Image.fromarray(padded)

        # Blur image
        blurred = pil_cropped_image.filter(ImageFilter.GaussianBlur(gaussian_blur))

        # Store in respective arrays to be saved
        cropped_images[i] = cropped
        blurred_cropped_images[i] = blurred

    print("Saving cropped/blurred..")
    np.save('./VOC_data/voc07_train_only_cropped.npy', cropped_images)
    np.save('./VOC_data/voc07_train_only_blurred_cropped.npy', blurred_cropped_images)

    sess.close()


    # traindata = np.load("./VOC_data/voc07_train1.npy")

    # sess = tf.InteractiveSession()

    # l = traindata.shape
    # print("starting")
    # train_padded = np.array([])
    # for i in range(2501):
    #     print(i)
    #     t = tf.image.resize_image_with_crop_or_pad(traindata[i], 227, 227)
    #     # t = tf.image.resize_images(traindata[i], 227, 227)
    #     padded = t.eval()
    #     print(padded.shape)
    #     train_padded = np.append(train_padded, padded)
    # sess.close()
    # np.save("./VOC_data/voc07_train_resize_227.npy", train_padded)
    # print("saving image..")
    # scipy.misc.imsave('./outfile.jpg', train_padded[0])
    

    # testdata = np.load("./VOC_data/voc07_test.npy")
    # sess = tf.InteractiveSession()

    # l = testdata.shape
    # test_padded = np.array([])
    # for i in range(l[0]):
    #     print(i)
    #     t = tf.image.resize_image_with_crop_or_pad(testdata[i], 500, 500)
    #     padded = t.eval()
    #     print(padded.shape)
    #     test_padded = np.append(test_padded, padded)
    # np.save('./VOC_data/voc07_test_padded.npy', test_padded)
    # sess.close()



if __name__ == "__main__":
    tf.app.run(main=main)

