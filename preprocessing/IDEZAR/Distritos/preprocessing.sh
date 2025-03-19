#!/bin/bash
rm -r data/IDEZAR/Distritos/refined
mkdir data/IDEZAR/Distritos/refined
cd tools
./openrefine-batch/openrefine-batch.sh \
-a ../data/IDEZAR/Distritos/raw/ \
-b ../preprocessing/IDEZAR/Distritos/ \
-c ../data/IDEZAR/Distritos/refined/ \
-e csv \
-f xml \
-i recordPath=feed \
-i guessCellValueTypes=false \
-m 4096M \
-RX
cd ..