#!/bin/bash
rm -r data/ZGZ/Agricultura/refined
mkdir data/ZGZ/Agricultura/refined
cd tools
./openrefine-batch/openrefine-batch.sh \
-a ../data/ZGZ/Agricultura/raw/ \
-b ../preprocessing/ZGZ/Agricultura/ \
-c ../data/ZGZ/Agricultura/refined/ \
-e csv \
-f xlsx \
-i sheets=0 \
-i trimStrings=true \
-i guessCellValueTypes=false \
-i ignoreLines=3 \
-i storeBlankRows=false \
-i storeBlankCellsAsNulls=false \
-i includeFileSources=true \
-i encoding=UTF-8 \
-m 4096M \
-RX \
cd ..