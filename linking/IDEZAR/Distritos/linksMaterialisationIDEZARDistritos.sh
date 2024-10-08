#!/bin/bash
data_directory='data/IDEZAR/Distritos/'
linking_directory='linking/IDEZAR/Distritos/'
linking_file=$linking_directory'linkingIDEZARDistritos.ttl'
data_file=$data_directory'linkingDataInProcess.csv'
config_file=$linking_directory'linkingConfigInProcess.ini'


for file in $data_directory'linked/*.csv' ; do
    cp $file $data_file
    output_name="$(basename -s .csv $file)_links.nt"
    
    echo [CONFIGURATION]>$config_file
    echo output_file = $data_directory'rdf/'$output_name>>$config_file
    echo number_of_processes=1 >>$config_file
    echo output_format=N-QUADS >>$config_file

    echo [DataSourceCSV]>>$config_file
    echo mappings=$linking_file>>$config_file
    echo file_path=$data_file>>$config_file

    python -m morph_kgc $config_file
    rm -r $config_file
    rm -r $data_file
done
