#!/bin/bash
rm -r data/ZGZ/Flota_municipal/refined
mkdir data/ZGZ/Flota_municipal/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/ZGZ/Flota_municipal/raw/ \
-b ../preprocessing/ZGZ/Flota_municipal/ \
-c ../data/ZGZ/Flota_municipal/refined/ \
-e csv \
-f xlsx \
-i sheets=0 \
-i sheets=1 \
-i trimStrings=true \
-i guessCellValueTypes=false \
-i storeBlankCellsAsNulls=false \
-i includeFileSources=true \
-i encoding=UTF-8 \
-m 4096M \
-RX
cd ..