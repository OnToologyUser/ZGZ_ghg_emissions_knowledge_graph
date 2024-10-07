cd ontology
cp usage_ontology.drawio usage_ontology.xml
curl -F data=@usage_ontology.xml https://chowlk.linkeddata.es/api | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['ttl_data'])" > usage_ontology.ttl
curl -F data=@usage_ontology.xml https://chowlk.linkeddata.es/api | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['errors'])"    
# rm usage_ontology.xml
cd ..