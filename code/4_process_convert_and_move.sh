#!/bin/sh

/opt/labelme_yolo_utils/convert_labelme2yolo.py -i /mnt/Data/graffiti/kgd/photos2/out/ -o /mnt/Data/graffiti/kgd/ -c /mnt/Data/graffiti/kgd/class_names.txt

mv ./photos2/*.jpg ./photos-orig/

mv ./photos2/out/* ./photos/

cp ./photos/*.json ./json/
