#!/bin/bash
rm -r data/ZGZ/Arbolado/refined
mkdir data/ZGZ/Arbolado/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/ZGZ/Arbolado/raw/ \
-b ../preprocessing/ZGZ/Arbolado/ \
-c ../data/ZGZ/Arbolado/refined/ \
-e csv \
-f xlsx \
-i sheets=0 \
-i trimStrings=true \
-i guessCellValueTypes=false \
-i storeBlankCellsAsNulls=false \
-i includeFileSources=true \
-i encoding=UTF-7 \
-m 4096M \
-RX \
cd ..