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
# ./mapping/ZGZ/Residencial/mapping_diagram_to_code.sh  # chowlk api doesn't support big files
    # using the Chowlk repo:
    # python3 converter.py ../USAGE-LD/mapping/ZGZ/Residencial/mapping_temp.xml ../USAGE-LD/mapping/ZGZ/Residencial/mapping.ttl

# ./mapping/ZGZ/Residencial/materialisationZGZResidencial.sh 
# ./mapping/IDEZAR/Barrios/materialisationIDEZARBarrios.sh 
# ./mapping/IDEZAR/Distritos/materialisationIDEZARDistritos.sh 

## validation (data)
# ./validation/ZGZ/Residencial/shapes_diagram_to_code.sh
# python validation/ZGZ/Residencial/validationZGZResidencial.py

## loading
# ./loading/join.sh
# ./loading/preload_graphdb.bat # for now running in windows with the db shutdown

## verification

## linking

# ./linking/IDEZAR/Distritos/reconcilingIDEZARDistritos.sh
# ./linking/IDEZAR/Distritos/linking_diagram_to_code.sh
# ./linking/IDEZAR/Distritos/linksMaterialisationIDEZARDistritos.sh

# ./linking/ZGZ/Residencial/reconcilingZGZResidencial.sh
# ./linking/ZGZ/Residencial/linking_diagram_to_code.sh
# ./linking/ZGZ/Residencial/linksMaterialisationZGZResidencial.sh

## publication
# ./publish/publish.bat

## exploitation

## maintainance
