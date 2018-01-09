# 单目标检测
## 一、相关论文

| 序号 | 时间 | 论文名字 | 会议 | git |
|-----|------|--------|------|-----|
|1|2015.12.8|SSD Deconvolutional Single Shot Detector|ECCV2016|
|2|2017.1.23|DSSD Deconvolutional Single Shot Detector|
|3|2017.5.26|R-SSD Enhancement of SSD by concatenating feature maps for object detection|
|4|2017.07.18|RUN：Residual Features and Unified Prediction Network for Single Stage Detection||[git](https://github.com/kmlee-snu/run)|
|5|2017.7.26|Detecting Small Signs from Large Images|
|6|2017.8.17|S3FD Single Shot Scale-invariant Face Detector|
|7|2016.8.24|Online Real-time Multiple Spatiotemporal Action Localisation and Prediction|ICCV 2017|[git](https://github.com/gurkirt/realtime-action-detection)|
|8|2017.8.27|Context-aware single-shot detector|
|9|2017.9.15|Feature-Fused SSD: Fast Detection for Small Objects|
|10|2017.11.18|Single-Shot Refinement Neural Network for Object Detection||[git](https://github.com/sfzhang15/RefineDet)||
|11|2017.11.27|Receptive Field Block Net for Accurate and Fast Object Detection||[git](https://github.com/ruinmessi/RFBNet)|
|12|2017.12.1|Single-Shot Object Detection with Enriched Semantics|
|13|2017.12.4|FSSD: Feature Fusion Single Shot Multibox Detector|
|14|2017.12.8|Weaving Multi-scale Context for Single Shot Detector|

## 二、相关方法对比
训练条件:VOC07+12<br>
对比条件: (T):Titanx Maxwell   (P):Titan X Pascal GPU
Speed(P)=2*Speed(T)
以下数据全部来自论文统计

|序号|方法|输入大小|基础网络|速度fps|mAP（VOC07)|mAP（VOC12)|备注|
|---|---|-------|-------|------|----------|-----------|---|
|1|SSD|300|VGG16|46|77.2|75.8|
|2|DSSD|300|Resnet-101|9.5|78.6|76.3|
|3|RefineDet|320|VGG16|40.3|80|78.1|
|4|DES|300|VGG16|34|79.5|77|67.8(P)|
|5|DSOD|300|DS/64-192-48-1|17.4|77.7|-|
|6|R-SSD|300|VGG16|37.1|78.5|-|
|7|RUN3WAY|300|VGG16|40|79.2|
|8|FSSD|300|VGG16|33|78.8|-|65.6(P)|
|9|DiCSSD|300|VGG16|40.8|78.1|-|-|
|10|DeCSSD|300|VGG16|39.8|77.6|
|11|Proposed element-sum model|300|VGG16|43|78.9|
|12|RFBNet|300|VGG16|43|80.5|
|13|RFBNet|300|VGG16|83|80.5|
|-|-|
|序号|方法|输入大小|基础网络|速度fps|mAP（VOC07)|mAP（VOC12)|备注|
|1|SSD|512|VGG16|19|79.8|78.5|
|2|DSSD|513|Resnet-101|5.5|81.5|80|
|3|**RefineDet**|512|VGG16|**24.1**|**81.8**|80.1|
|4|DES|512|VGG16|14|81.6|80.2|27.2(P)|
|5|R-SSD|512|VGG16|15.8|80.8|
|6|RUN3WAY|512|VGG16|19.5|80.9|
|7|FSSD|512|VGG16|18|80.9|-|35.7(P)|
|8|**RFB**|512|VGG16|**18**|**82.2**|
|9|RFBNet|512|VGG16|38|82.23|
