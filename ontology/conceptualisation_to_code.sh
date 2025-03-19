directory='ontology'
file_name='ontology'

cp $directory/$file_name'.drawio' $directory/$file_name'_temp.xml'
docker run -v ./$directory:/tmp --rm  chowlk-chowlk:latest  bin/bash  -c "python3 home/app/converter.py tmp/$file_name'_temp.xml' tmp/$file_name.ttl"
rm $directory/$file_name'_temp.xml'
