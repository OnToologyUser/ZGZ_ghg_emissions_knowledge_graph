#!/bin/bash
rm -r data/ZGZ/Residencial/linked
mkdir data/ZGZ/Residencial/linked
cd tools
./openrefine-batch/openrefine-batch.sh \
-a ../data/ZGZ/Residencial/refined/ \
-b ../linking/ZGZ/Residencial/ \
-c ../data/ZGZ/Residencial/linked/ \
-e csv \
-f csv \
-i trimStrings=true \
-i guessCellValueTypes=false \
-i storeBlankCellsAsNulls=false \
-i encoding=UTF-8 \
-m 4096M \
-RX \
cd ..