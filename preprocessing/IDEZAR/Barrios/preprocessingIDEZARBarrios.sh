#!/bin/bash
rm -r data/IDEZAR/Barrios/refined
mkdir data/IDEZAR/Barrios/refined
cd tools
./openrefine-batch-master/openrefine-batch.sh \
-a ../data/IDEZAR/Barrios/raw/ \
-b ../preprocessing/IDEZAR/Barrios/ \
-c ../data/IDEZAR/Barrios/refined/ \
-e csv \
-f xml \
-i recordPath=feed \
-i guessCellValueTypes=false \
-m 4096M \
-RX
cd ..