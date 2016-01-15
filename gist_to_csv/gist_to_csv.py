import os
import csv
import numpy as np

path_to_all_gist = "/media/virgil/Storage/FACULTATE/An3/Sem1/IA/Proiect/Images+GIST/gist_files"
csvfile = "/media/virgil/Storage/FACULTATE/An3/Sem1/IA/Proiect/Images+GIST/result.csv"

# each directory (class) has a label
label = 0

with open(csvfile, "wb") as output:
    writer = csv.writer(output)
    for directory_name in os.listdir(path_to_all_gist):
        if "_gist" in directory_name:
            label += 1
            directory_path = os.path.join(path_to_all_gist, directory_name)
            print directory_path

            # inside this directory get all .gist files and add them as lines in the csv
            for file_name in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file_name)
                # print file_path

                # read the content of the file into an array
                file_content_array = np.loadtxt(file_path, delimiter="\n")

                # having the content, place it in the csv
                file_content_array = np.insert(file_content_array, 0, label)
                writer.writerow(file_content_array)