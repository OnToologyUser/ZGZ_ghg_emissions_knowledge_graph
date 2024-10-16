#!/bin/bash
rm -r data/ZGZ/Aviacion/refined
mkdir data/ZGZ/Aviacion/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/ZGZ/Aviacion/raw/ \
-b ../preprocessing/ZGZ/Aviacion/ \
-c ../data/ZGZ/Aviacion/refined/ \
-e csv \
-f xlsx \
-i sheets=0 \
-i trimStrings=true \
-i guessCellValueTypes=false \
-i storeBlankCellsAsNulls=false \
-i includeFileSources=true \
-i encoding=UTF-8 \
-m 4096M \
-RX
cd ..