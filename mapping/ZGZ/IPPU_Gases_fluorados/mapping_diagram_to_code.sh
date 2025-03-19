mapping_directory='mapping/ZGZ/IPPU_Gases_fluorados/'
mapping_file_name='mapping'

cp $mapping_directory$mapping_file_name'.drawio' $mapping_directory'mapping_temp.xml'
docker run -v ./mapping/ZGZ/IPPU_Gases_fluorados:/tmp --rm  chowlk-chowlk:latest  bin/bash  -c "python3 home/app/converter.py tmp/mapping_temp.xml tmp/mapping.ttl"
rm $mapping_directory'mapping_temp.xml'
