# here we get rid of that added dimension and plot the image
def visualize_cnn(model, cat):
    # Keras expects batches of images, so we have to add a dimension to trick it into being nice
    cat_batch = np.expand_dims(cat,axis=0)
    conv_cat = model.predict(cat_batch)
    conv_cat = np.squeeze(conv_cat, axis=0)
    print conv_cat.shape
    plt.imshow(conv_cat.transpose(2, 1, 0))