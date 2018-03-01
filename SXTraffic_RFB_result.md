Priv_Shanxitraffic-Benchmark
Object Detection Performance on Priv_Shanxitraffic About Priv_Shanxitraffic:

v0.2<br>
13,798 images totally: train set 11,639 images, val set 2,159 images
7(9) categories including background, car, truck, bus, motorcycle, bicycle, person(pedestrian, rider, driver)

v0.2.1<br> 
remove some low quality images
12,196 images totally: train set 10,410 images, val set 1,786 images
7(9) categories including background, car, truck, bus, motorcycle, bicycle, person(pedestrian, rider, driver)

v0.2.1<br> 

**mAP best in RFCN is 0.622**

- **exp1** 300*300 300epoch
300 speed:22.77fps forward speed：83fps
pure test speed(without load net structure)：83fps

|class|100/300epoch_val|220/300epoch_val|250/300epoch_val|240/240epoch_val|100epoch_train|220epoch_train|
|-----|----------------|----------------|----------------|----------------|--------------|--------------|
|car  |0.895|0.893|0.893|0.894|0.908|0.908|
|truck|0.297|0.332|0.335|0.307|0.905|0.897|
|bus  |0.818|0.824|0.826|0.783|0.891|0.862|
|motorcycle|0.692|0.719|0.723|0.705|0.900|0.907|
|bicycle|0.222|0.284|0.285|0.220|0.789|0.814|
|person|0.655|0.693|0.690|0.687|0.777|0.860|
|**mAP**|0.5965|0.6241|0.6252|0.5992|0.8616|0.8748|

- **exp2** 300*300 240epoch
s:300 240epoch train time 17.5h

|epoch/total_epoch|val|train|
|-----------------|---|-----|
|240/240 |**0.5992**|0.8846|
|220/240 |0.6012    |0.8838|
|200/240 |0.5957    |0.8835|
|110/240 |0.5888    |0.8744|
|10/240  |0.5062    |0.7818|


 - **exp3** 512*512 240epoch
s:512 240epoch train time
test speed:10.19fps forward speed：50fps

|epoch/total_epoch|val|train|
|-----------------|---|-----|
|240/240 |**0.6794**|0.8915 |
|220/240 |0.6798    |0.8913 |
|200/240 |0.6711    |0.8912 |
|110/240 |0.6658    |0.8842 |
|10/240  |0.5424    |0.8083 |
