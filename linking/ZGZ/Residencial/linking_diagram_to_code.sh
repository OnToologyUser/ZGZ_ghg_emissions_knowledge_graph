linking_directory='linking/ZGZ/Residencial/'
linking_file_name='linkingZGZResidencial'

cp $linking_directory$linking_file_name'.drawio' $linking_directory'linking_temp.xml'
curl -F data=@$linking_directory'linking_temp.xml' https://chowlk.linkeddata.es/api | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['ttl_data'])" > $linking_directory$linking_file_name'.ttl'
rm $linking_directory'linking_temp.xml'
