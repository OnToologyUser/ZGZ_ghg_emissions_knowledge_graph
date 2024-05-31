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
-i trimStrings=true \
-i guessCellValueTypes=false \
-i storeBlankCellsAsNulls=false \
-i encoding=UTF-8 \
-m 4096M \
-RX \
cd ..