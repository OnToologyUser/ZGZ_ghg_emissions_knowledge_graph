#!/bin/bash
rm -r data/ZGZ/Institucional_y_servicios/refined
mkdir data/ZGZ/Institucional_y_servicios/refined
cd tools
./openrefine-batch/openrefine-batch.sh \
-a ../data/ZGZ/Institucional_y_servicios/raw/ \
-b ../preprocessing/ZGZ/Institucional_y_servicios/ \
-c ../data/ZGZ/Institucional_y_servicios/refined/ \
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