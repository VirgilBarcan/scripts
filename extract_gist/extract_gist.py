import os
from PIL import Image
import numpy as np
import leargist

# the path to the directory that contains all images
# the directory should have different folders for each sentiment
path_to_all_images = "path/to/folder/with/images"

for directory_name in os.listdir(path_to_all_images):
    directory_path = os.path.join(path_to_all_images, directory_name)
    print directory_path

    # build _gist directory
    gist_directory_path = os.path.join(path_to_all_images, directory_name + "_gist")
    os.makedirs(gist_directory_path)

    # inside this directory get all image files, extract the GIST descriptor values and
    # save the descriptor values to a .gist file with the same name as the image file name
    for file_name in os.listdir(directory_path):
        image_path = os.path.join(directory_path, file_name)
        file_path = os.path.join(gist_directory_path, file_name + ".gist")
        
        # construct an Image object to store the image file
        image = Image.open(image_path)
        
        # extract the GIST descriptors by calling the library
        descriptors = leargist.color_gist(image)

        # save the descriptors to a file, each value on a different row
        np.savetxt(file_path, descriptors, delimiter='\n')
