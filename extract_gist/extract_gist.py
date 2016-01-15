import os
from PIL import Image
import numpy as np
import leargist

path_to_all_gist = "/media/virgil/Storage/FACULTATE/An3/Sem1/IA/Proiect/Images+GIST/resDataReduced"

for directory_name in os.listdir(path_to_all_gist):
    directory_path = os.path.join(path_to_all_gist, directory_name)
    print directory_path

    # build _gist directory
    gist_directory_path = os.path.join(path_to_all_gist, directory_name + "_gist")
    os.makedirs(gist_directory_path)

    # inside this directory get all .gist files and add them as lines in the csv
    for file_name in os.listdir(directory_path):
        image_path = os.path.join(directory_path, file_name)
        file_path = os.path.join(gist_directory_path, file_name + ".gist")
        # print file_path

        image = Image.open(image_path)
        descriptors = leargist.color_gist(image)

        np.savetxt(file_path, descriptors, delimiter='\n')