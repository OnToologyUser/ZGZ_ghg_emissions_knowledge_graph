#!/bin/bash
rm -r data/ZGZ/Residencial/refined
mkdir data/ZGZ/Residencial/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/ZGZ/Residencial/raw/ \
-b ../preprocessing/ZGZ/Residencial/ \
-c ../data/ZGZ/Residencial/refined/ \
-e csv \
-f xlsx \
-i sheets=0 \
-m 4096M \
-R \
-X \    
cd ..