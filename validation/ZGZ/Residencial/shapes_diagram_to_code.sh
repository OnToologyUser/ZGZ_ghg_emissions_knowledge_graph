validation_directory='validation/ZGZ/Residencial/'
shapes_file_name='shapesZGZResidencial'

cp $validation_directory$shapes_file_name'.drawio' $validation_directory'shapes_temp.xml'
curl -F data=@$validation_directory'shapes_temp.xml' https://chowlk.linkeddata.es/api | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['ttl_data'])" > $validation_directory$shapes_file_name'.ttl'
rm $validation_directory'shapes_temp.xml'
