#!/bin/bash
rm -r data/ZGZ/Industrial/refined
mkdir data/ZGZ/Industrial/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/ZGZ/Industrial/raw/ \
-b ../preprocessing/ZGZ/Industrial/ \
-c ../data/ZGZ/Industrial/refined/ \
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