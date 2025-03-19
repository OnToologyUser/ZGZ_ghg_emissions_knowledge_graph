#!/bin/bash
rm -r data/IDEZAR/Distritos/linked
mkdir data/IDEZAR/Distritos/linked
cd tools
./openrefine-batch/openrefine-batch.sh \
-a ../data/IDEZAR/Distritos/refined/ \
-b ../linking/IDEZAR/Distritos/ \
-c ../data/IDEZAR/Distritos/linked/ \
-e csv \
-f csv \
-i trimStrings=true \
-i guessCellValueTypes=false \
-i storeBlankCellsAsNulls=false \
-i encoding=UTF-8 \
-m 4096M \
-RX \
cd ..