#!/bin/bash
## extraction
# python extraction/IDEZAR/Barrios/extractionIDEZARBarrios.py
# python extraction/IDEZAR/Distritos/extractionIDEZARDistritos.py

## conceptualisation
# ./ontology/conceptualisation_to_code.sh

## preprocessing
# ./preprocessing/ZGZ/Residencial/preprocessingZGZResidencial.sh
# ./preprocessing/IDEZAR/Barrios/preprocessingIDEZARBarrios.sh
# ./preprocessing/IDEZAR/Distritos/preprocessingIDEZARDistritos.sh

## mapping
# ./mapping/ZGZ/Residencial/mapping_diagram_to_code.sh 

# ./mapping/ZGZ/Residencial/materialisationZGZResidencial.sh 
# ./mapping/IDEZAR/Barrios/materialisationIDEZARBarrios.sh 
# ./mapping/IDEZAR/Distritos/materialisationIDEZARDistritos.sh 
# ./mapping/join.sh


## validation (data)



## loading
# ./loading/preload_graphdb.bat # for now running in windows with the db shutdown

## verification (ontology)

## linking

## publication
# ./publish/publish.bat

## exploitation

## maintainance
