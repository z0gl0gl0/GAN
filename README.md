# GAN_reading_club

To train the GAN, you need to enter this command line :
``` ./training_dataset.py <name of dataset> <number of images of the dataset> <number of epochs> <number of epochs between each time you save images> ```
EXAMPLE :
``` ./training_dataset.py kagle_sup256 2973 5000 1000 ```



To generate images, you must train the GAN first to have two `.h5` files. Next, enter this command line :
``` ./generation.py <name of dataset> <number of epoch used to train the model> <number of images you want> ```
EXAMPLE :
``` ./generation.py kagle_256 5000 100 ```

Note : If you don't remember the name of the dataset and the number of epochs you used, the name of the generator model is `generator_model_<dataset>_<number of epochs>.h5`.
