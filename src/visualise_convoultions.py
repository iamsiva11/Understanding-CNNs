# here we get rid of that added dimension and plot the image
def visualize_cnn(model, cat):
    # Keras expects batches of images, so we have to add a dimension to trick it into being nice
    cat_batch = np.expand_dims(cat,axis=0)
    conv_cat = model.predict(cat_batch)
    conv_cat = np.squeeze(conv_cat, axis=0)
    print conv_cat.shape
    plt.imshow(conv_cat.transpose(2, 1, 0))

# Lets create a model with 1 Convolutional layer
model = Sequential()
model.add(Convolution2D(3,    # number of filter layers
                        3,    # y dimension of kernel (we're going for a 3x3 kernel)
                        3,    # x dimension of kernel
                        input_shape=cat.shape))

# Keras expects batches of images, so we have to add a dimension to trick it into being nice
cat_batch = np.expand_dims(cat,axis=0)

conv_cat = model.predict(cat_batch)

def nice_cat_printer(model, cat):
    '''prints the cat as a 2d array'''
    cat_batch = np.expand_dims(cat,axis=0)
    conv_cat2 = model.predict(cat_batch)

    conv_cat2 = np.squeeze(conv_cat2, axis=0)
    print conv_cat2.shape
    conv_cat2 = conv_cat2.reshape(conv_cat2.shape[:2])

    print conv_cat2.shape
    plt.imshow(conv_cat2)







