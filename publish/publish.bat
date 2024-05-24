copy "data\rdf-file.nt" "tools/Helio/mappings/data/rdf-file.nt"
cd "tools/Helio"
java -jar publisher-0.3.13.jar --server.port=8080 --mappings=mappings