import json
import os


"""
cd datasets
mkdir -p mix_mot_ch/annotations
cp mot/annotations/val_half.json mix_mot_ch/annotations/val_half.json
cp mot/annotations/test.json mix_mot_ch/annotations/test.json
cd mix_mot_ch
ln -s ../mot/train mot_train
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val
cd ..
"""

mot17_json = json.load(open('../MOT17/annotations/train_half.json','r'))


img_list = list()
for img in mot17_json['images']:
    img['file_name'] = 'mot17_train/' + img['file_name']
    img_list.append(img)

ann_list = list()
for ann in mot17_json['annotations']:
    ann_list.append(ann)

video_list = mot17_json['videos']
category_list = mot17_json['categories']

print('mot17')

max_img = 10000
max_ann = 2000000
max_video = 10


mot20_json = json.load(open('../MOT20/annotations/train_half.json','r'))

img_list = list()
for img in mot20_json['images']:
    img['file_name'] = 'mot20_train/' + img['file_name']
    img_list.append(img)

ann_list = list()
for ann in mot20_json['annotations']:
    ann_list.append(ann)

video_list = mot20_json['videos']
category_list = mot20_json['categories']

print('mot20')
max_img = 10000
max_ann = 2000000
max_video = 10

mix_json = dict()
mix_json['images'] = img_list
mix_json['annotations'] = ann_list
mix_json['videos'] = video_list
mix_json['categories'] = category_list
json.dump(mix_json, open('mix_dataset/annotations/train.json','w'))
