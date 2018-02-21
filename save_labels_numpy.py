import tensorflow as tf
import numpy as np

def main(unused_arg):
    filename_queue = tf.train.string_input_producer(["./VOC_data/trainval_labels.csv", "./VOC_data/test_labels.csv"])
    reader = tf.TextLineReader()
    train_key, train_vals = reader.read(filename_queue)
    test_key, test_vals = reader.read(filename_queue)

    # Default values, in case of empty columns. Also specifies the type of the
    # decoded result.
    record_defaults = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
    name,aeroplane,bicycle,bird,boat,bottle,bus,car,cat,chair,cow,diningtable,dog,horse,motorbike,person,pottedplant,sheep,sofa,train,tvmonitor = tf.decode_csv(train_vals, record_defaults=record_defaults)
    multi_trainlabels = tf.stack([aeroplane,bicycle,bird,boat,bottle,bus,car,cat,chair,cow,diningtable,dog,horse,motorbike,person,pottedplant,sheep,sofa,train,tvmonitor])

    test_name,test_aeroplane,test_bicycle,test_bird,test_boat,test_bottle,test_bus,test_car,test_cat,test_chair,test_cow,test_diningtable,test_dog,test_horse,test_motorbike,test_person,test_pottedplant,test_sheep,test_sofa,test_train,test_tvmonitor = tf.decode_csv(test_vals, record_defaults=record_defaults)
    multi_testlabels = tf.stack([test_aeroplane,test_bicycle,test_bird,test_boat,test_bottle,test_bus,test_car,test_cat,test_chair,test_cow,test_diningtable,test_dog,test_horse,test_motorbike,test_person,test_pottedplant,test_sheep,test_sofa,test_train,test_tvmonitor])


    with tf.Session() as sess:
    # Start populating the filename queue.
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)

        trainlabels = np.array([])
        testlabels = np.array([])
        for i in range(5011):
            # Retrieve a single instance:
            print("GDAKMGDAKLGDKLFGKLFGALAFGJL " + str(i))
            example = sess.run([multi_trainlabels])
            np.append(trainlabels, example)
            # print(example)
            # print(type(multi_labels))
        
        for i in range(4952):
            example = sess.run([multi_testlabels])
            np.append(testlabels, example)


    coord.request_stop()
    coord.join(threads)

    np.save('./VOC_data/voc07_train_labels.npy', trainlabels)
    np.save('./VOC_data/voc07_test_labels.npy', testlabels)

if __name__ == "__main__":
    tf.app.run(main=main)
