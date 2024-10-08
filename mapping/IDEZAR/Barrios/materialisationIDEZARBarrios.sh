#!/bin/bash
data_directory='data/IDEZAR/Barrios/'
mapping_directory='mapping/IDEZAR/Barrios/'
mapping_file=$mapping_directory'mappingIDEZARBarrios.ttl'
data_file=$data_directory'dataInProcess.csv'
config_file=$mapping_directory'configInProcess.ini'


for file in $data_directory'refined/*.csv' ; do
    cp $file $data_file
    output_name="$(basename -s .csv $file).nt"
    
    echo [CONFIGURATION]>$config_file
    echo output_file = $data_directory'rdf/'$output_name>>$config_file
    echo number_of_processes=1 >>$config_file
    echo output_format=N-TRIPLES >>$config_file

    echo [DataSourceCSV]>>$config_file
    echo mappings=$mapping_file>>$config_file
    echo file_path=$data_file>>$config_file

    python -m morph_kgc $config_file
    rm -r $config_file
    rm -r $data_file
done
