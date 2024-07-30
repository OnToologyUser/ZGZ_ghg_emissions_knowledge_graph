#!/bin/bash
rm -r data/ZGZ/Transporte/refined
mkdir data/ZGZ/Transporte/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/ZGZ/Transporte/raw/ \
-b ../preprocessing/ZGZ/Transporte/ \
-c ../data/ZGZ/Transporte/refined/ \
-e csv \
-f xlsx \
-i sheets=0 \
-i trimStrings=true \
-i guessCellValueTypes=false \
-i storeBlankCellsAsNulls=false \
-i encoding=UTF-8 \
-m 4096M \
cd ..