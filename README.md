# 2022 Introduction of Deep Learning Final Project
## Multi-Object Tracking

## ByteTrack

##### Install
1. Anaconda 환경에서 가상환경 생성
```
conda create -n bytetrack python=3.7
```
2. 가상환경 활성화
```
conda activate bytetrack
```
3. git clone and change directory
```
git clone https://github.com/JYEDU/DI_ByteTrack.git
cd ByteTrack
```
4. 환경 설정
```
pip3 install -r requirements.txt
python3 setup.py develop
```
5. pycocotools 설치
```
pip3 install cython; pip3 install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
```
6. 기타 필요한 것 설치
```
pip3 install cython_bbox
```
7. Docker Build
```
docker build -t bytetrack:latest .

# Startup sample
mkdir -p pretrained && \
mkdir -p YOLOX_outputs && \
xhost +local: && \
docker run --gpus all -it --rm \
-v $PWD/pretrained:/workspace/ByteTrack/pretrained \
-v $PWD/datasets:/workspace/ByteTrack/datasets \
-v $PWD/YOLOX_outputs:/workspace/ByteTrack/YOLOX_outputs \
-v /tmp/.X11-unix/:/tmp/.X11-unix:rw \
--device /dev/video0:/dev/video0:mwr \
--net=host \
-e XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
-e DISPLAY=$DISPLAY \
--privileged \
bytetrack:latest
```

##### Dataset Preparation
1. [MOT17](https://motchallenge.net/data/MOT17/), [MOT20](https://motchallenge.net/data/MOT20/)를 경로에 맞게 다운로드 한다.
```
├──ByteTrack
├──MOT17
│    ├──train
│    └──test
├──MOT20
     ├──train
     └──test
```
2. 데이터 전처리를 위해 먼저, COCO 형식으로 포맷을 변경한다.
```
python3 tools/convert_mot17_to_coco.py
python3 tools/convert_mot20_to_coco.py
```
3. 데이터 전처리를 위해 다른 데이터셋들을 섞어준다.
```
python3 tools/mix_data_ablation.py
```

##### Train
1. 실험환경에 맞춰 모델을 훈련한다.
```
python3 tools/train.py --exp_file exps/example/mot/yolox_x_ablation.py --devices 1 --batch-size 4 --fp16 --occupy --ckpt pretrained/yolox_x.pth

```

##### Test
```
python3 tools/track.py -f exps/example/mot/track_mot17_jh.py -c YOLOX_outputs/yolox_x_ablation/last_epoch_ckpt.pth.tar -b 1 -d 1 --fp16 --fuse
```

## Reference
1. [[Dataset](https://motchallenge.net/)] MOT17, MOT20
2. [[Github](https://github.com/ifzhang/ByteTrack)] ByteTrack
3. [Paper] Paper Patrick Dendorfer, Aljoša Ošep, Anton Milan, Konrad Schindler, Daniel Cremers, Ian Reid, Stefan Roth, and Laura Leal-Taixé, "Motchallenge: A benchmark for single-camera multiple target tracking." International Journal of Computer Vision 129.4, 2021
4. [Paper] Patrick Dendorfer, Hamid Rezatofighi, Anton Milan, Javen Shi, Daniel Cremers, Ian Reid, Stefan Roth, Konrad Schindler, and Laura Leal-Taixé, "Mot20: A benchmark for multi object tracking in crowded scenes." arXiv, 2020
5. [Paper] Yifu Zhang, Peize Sun, Yi Jiang, Dongdong Yu, Fucheng Weng, Zehuan Yuan, Ping Luo, Wenyu Liu, and Xinggang Wang, "ByteTrack: Multi-Object Tracking by Associating Every Detection Box." arXiv, 2021
6. [Paper] Yunhao Du, Yang Song, Bo Yang, and Yanyun Zhao, "StrongSORT: Make DeepSORT Great Again." arXiv, 2022
7. [Paper] Fangao Zeng, Bin Dong, Yuang Zhang, Tiancai Wang, Xiangyu Zhang, and Yichen Wei, "Motr: End-to-end multiple-object tracking with transformer." arXiv, 2021
8. [Paper] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and Sergey Zagoruyko, "End-to-end object detection with transformers." European conference on computer vision. Springer, Cham, 2020
9. [Paper] Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, and Jian Sun, "Yolox: Exceeding yolo series in 2021." arXiv, 2021
10. [Paper] Wojke, Nicolai, Alex Bewley, and Dietrich Paulus. "Simple online and realtime tracking with a deep association metric." 2017 IEEE international conference on image processing (ICIP). IEEE, 2017.
