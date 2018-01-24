| 序号 | 文件名 | 训练集合 | 测试集合 | 结果 | 速度fps | 训练信息 | 测试信息 |car|truck|bus|motorcycle|bicycle|person|
|------|------|---------|---------|-----|------|--------|---------|---|-----|---|----------|-------|------|
|1|Refine2|val| val|0.8620|9.689|512*384,7.5W,<br>batch=32,2GPU|single,nms|0.875|0.850|0.921|0.847|0.886|0.793|0.862|
|2|-|val|val|0.8212|8.830|-|single,nms*2|0.828|0.820|0.921|0.844|0.728|0.786|0.821|
|3|-|val|val|0.8615|9.394|-|single,soft_nms|0.872|0.848|0.921|0.848|0.881|0.800|0.861|
|4|-|val|val|0.8689|0.408|-|multi,soft_nms|0.876|0.856|0.921|0.854|0.907|0.800|0.869|
|4+|-|val|train|0.4429|-|-|single,soft_nms|0.771|0.295|0.523|0.408|0.185|0.475|0.443|
|5|Refine3|train|val|0.5198|10.368|512*384 **7w** batch=32,2|single,soft_nms|0.828|0.165|0.767|0.625|0.174|0.559|0.520|
|6|-|train| val|0.5175|10fps|-|single,nms|0.830|0.165|0.763|0.615|0.183|0.549|0.517|
|7|Refine3|train|val|0.5161|9.75|512*384 **7.5w** batch=32,2|single,soft_nms|0.824|0.170|0.764|0.619|0.163|0.556|0.516|
|8|-|train|val|0.5134|10|-|single,nms|0.827|0.169|0.756|0.611|0.173|0.545|0.513|
|9|-|train|train|0.3767|1.7|512*384 **7.5w** batch=32,2|single,nms|0.595|0.234|0.771|0.152|0.097|0.410|0.377|
|10|-|train|train|0.3816|1.7|-|single,soft_nms|0.596|0.238|0.775|0.155|0.103|0.424|0.382|
|11|Refine4|train|train|0.4316|9|512*384 **9w/15w** batch=32,2|single,soft_nms|0.651|0.375|0.808|0.188|0.122|0.446|0.432|
|11+|-|train|val|0.4948|9|-|-|0.863|0.179|0.744|0.518|0.156|0.508|0.495|
|12|se-resnet50|train|val|0.4564|-|ms-ohem-multigrid|-|

Refine4的实验结果

| num | iter_num |lr|test on train|test on val| 
|---|--------|--|-------------|-----------|
|1|6w|0.001|0.2397|0.1953|
|2|7w|-|0.2805|0.2401|
|3|8w|-|0.4140|0.4837|
|4|9w|-|0.4316 |0.4948|
|5|10w|0.0001|0.4640|0.4969|
|6|11w|-|0.3942|0.5340|
|7|12w|-|0.3548|0.4228|
|8|12.5w|0.00001|0.3678|0.4881
|9|13w|-|0.3850|0.5610|
|10|14w|-|0.3829|0.5549|
|11|15w|-|0.3791|0.5494|

**loss log result**:
- **Refine 2**：训练集：val
1. loss
<img align="right" src="https://github.com/LilacYue/det/blob/master/Re2-val2val_7.5w.png">

- **Refine 4**: 训练集：train
1. loss
<img align="right" src="https://github.com/LilacYue/det/blob/master/Re4loss.jpg">
2. ODM loss
<img align="right" src="https://github.com/LilacYue/det/blob/master/Re4ODM.jpg">
3. ARM loss
<img align="right" src="https://github.com/LilacYue/det/blob/master/Re4ARM.jpg">
