#!/bin/bash
## extraction
python extraction/IDEZAR/Distritos/extraction.py

## conceptualisation
./ontology/conceptualisation_to_code.sh

## preprocessing # raw files names should not include whitespaces
./preprocessing/IDEZAR/Distritos/preprocessing.sh
./preprocessing/ZGZ/Residencial/preprocessing.sh
./preprocessing/ZGZ/Industrial/preprocessing.sh
./preprocessing/ZGZ/IPPU_Gases_fluorados/preprocessing.sh
./preprocessing/ZGZ/Residuos/preprocessing.sh 
./preprocessing/ZGZ/Arbolado/preprocessing.sh 
./preprocessing/ZGZ/Ganaderia/preprocessing.sh 
./preprocessing/ZGZ/Transporte/preprocessing.sh
python3 preprocessing/ZGZ/Transporte/blank_column_cli.py asWKT data/ZGZ/Transporte/refined/BBDD_Transp_Carretera_TPrivado_2021_v001.csv # Removed conflictive polygons
./preprocessing/ZGZ/Agricultura/preprocessing.sh
./preprocessing/ZGZ/Flota_municipal/preprocessing.sh
./preprocessing/ZGZ/Aviacion/preprocessing.sh

## mapping and materialisation
./mapping/IDEZAR/Distritos/mapping_diagram_to_code.sh  
./mapping/IDEZAR/Distritos/materialisation.sh 
./mapping/ZGZ/Residencial/mapping_diagram_to_code.sh  
./mapping/ZGZ/Residencial/materialisation.sh 
./mapping/ZGZ/Industrial/mapping_diagram_to_code.sh  
./mapping/ZGZ/Industrial/materialisation.sh 
./mapping/ZGZ/IPPU_Gases_fluorados/mapping_diagram_to_code.sh  
./mapping/ZGZ/IPPU_Gases_fluorados/materialisation.sh 
./mapping/ZGZ/Residuos/mapping_diagram_to_code.sh  
./mapping/ZGZ/Residuos/materialisation.sh 
./mapping/ZGZ/Arbolado/mapping_diagram_to_code.sh  
./mapping/ZGZ/Arbolado/materialisation.sh 
./mapping/ZGZ/Ganaderia/mapping_diagram_to_code.sh 
./mapping/ZGZ/Ganaderia/materialisation.sh 
./mapping/ZGZ/Transporte/mapping_diagram_to_code.sh  
./mapping/ZGZ/Transporte/materialisation.sh 
./mapping/ZGZ/Agricultura/mapping_diagram_to_code.sh
./mapping/ZGZ/Agricultura/materialisation.sh
./mapping/ZGZ/Flota_municipal/mapping_diagram_to_code.sh  
./mapping/ZGZ/Flota_municipal/materialisation.sh
./mapping/ZGZ/Aviacion/mapping_diagram_to_code.sh  
./mapping/ZGZ/Aviacion/materialisation.sh

## linking
./linking/IDEZAR/Distritos/reconciling.sh
./linking/IDEZAR/Distritos/linking_diagram_to_code.sh
./linking/IDEZAR/Distritos/links_materialisation.sh
./linking/ZGZ/Residencial/reconciling.sh
./linking/ZGZ/Residencial/linking_diagram_to_code.sh
./linking/ZGZ/Residencial/links_materialisation.sh

## loading
./loading/join.sh
python3 ./loading/zip.py
./loading/load_graphdb.sh 
./loading/run_graphdb.sh
