#!/bin/bash
rm -r data/ZGZ/Residuos/refined
mkdir data/ZGZ/Residuos/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/ZGZ/Residuos/raw/ \
-b ../preprocessing/ZGZ/Residuos/ \
-c ../data/ZGZ/Residuos/refined/ \
-e csv \
-f xlsx \
-i sheets=0 \
-i trimStrings=true \
-i guessCellValueTypes=false \
-i storeBlankCellsAsNulls=false \
-i includeFileSources=true \
-i encoding=UTF-8 \
-m 4096M \
-RX \
cd ..