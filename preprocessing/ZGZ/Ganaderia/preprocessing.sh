#!/bin/bash
rm -r data/ZGZ/Ganaderia/refined
mkdir data/ZGZ/Ganaderia/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/ZGZ/Ganaderia/raw/ \
-b ../preprocessing/ZGZ/Ganaderia/ \
-c ../data/ZGZ/Ganaderia/refined/ \
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