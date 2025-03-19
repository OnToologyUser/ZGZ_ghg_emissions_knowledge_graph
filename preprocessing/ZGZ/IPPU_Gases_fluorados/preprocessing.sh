#!/bin/bash
rm -r data/ZGZ/IPPU_Gases_fluorados/refined
mkdir data/ZGZ/IPPU_Gases_fluorados/refined
cd tools
./openrefine-batch/openrefine-batch.sh \
-a ../data/ZGZ/IPPU_Gases_fluorados/raw/ \
-b ../preprocessing/ZGZ/IPPU_Gases_fluorados/ \
-c ../data/ZGZ/IPPU_Gases_fluorados/refined/ \
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