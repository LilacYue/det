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

| 序号 |size| 单个epcho的时间 | 预计训练时间 | 测试速度 | 100epoch val | 100epoch train | 220epoch val | 220epoch train |
|-----|----|----------------|-----------|---------|--------------|----------------|--------------|----------------|
|1|300|9'35|36h|22.77|0.5965|0.8616|0.6241|0.8748|
|2|500|9'4|36h|21.86|0.5973|0.8650|0.5945|0.8769|

**mAP best in RFCN is 0.622**

300 speed:22.77fps 
pure test speed(without load net structure)：83fps

|class|100epoch_val|220epoch_val|100epoch_train|220epoch_train|
|-----|------------|------------|--------------|--------------|
|car|0.895|0.893|0.908|0.908|
|truck|0.297|0.332|0.905|0.897|
|bus|0.818|0.824|0.891|0.862|
|motorcycle|0.692|0.719|0.900|0.907|
|bicycle|0.222|0.284|0.789|0.814|
|person|0.655|0.693|0.777|0.860|
|**mAP**|0.5965|0.6241|0.8616|0.8748|


500 speed:21.76fps 
pure test speed(without load net structure)：73fps

|class|100epoch_val|220epoch_val|100epoch_train|220epoch_train|
|-----|------------|------------|--------------|--------------|
|car|0.892|0.892|0.908|0.909|
|truck|0.316|0.209|0.909|0.908|
|bus|0.829|0.797|0.906|0.865|
|motorcycle|0.675|0.717|0.898|0.907|
|bicycle|0.213|0.257|0.787|0.813|
|person|0.658|0.694|0.781|0.861|
|**mAP**|0.5973|0.5945|0.8650|0.8769|
