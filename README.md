# GAN Reading Club

To train the GAN, you need to enter this command line :

``` ./training_dataset.py <dataset> <N_images> <N_epochs> <N_save> ```

with `N_images` the number of images used in the dataset, `N_epochs` the number of epochs and `N_save` the number of epochs between two saves.

EXAMPLE :
``` ./training_dataset.py kagle_sup256 2973 5000 1000 ```

You will find in `images` images saved at each `N_save` epochs.

Note : Please put your datasets in `dataset`.


To generate images, you must train the GAN first to have two `.h5` files. Next, enter this command line :

``` ./generation.py <name of dataset> <number of epoch used to train the model> <number of images you want> ```

EXAMPLE :
``` ./generation.py kagle_256 5000 100 ```

You will find in `resultats` results of the generation of images.

Note : If you don't remember the name of the dataset and the number of epochs you used, the name of the generator model is `generator_model_<dataset>_<number of epochs>.h5`.
