copy "validation\ZGZ\geoSHACL\report.ttl" "tools\Helio\mappings\data\rdf-file.ttl"
cd "tools/Helio"
java -jar publisher-0.3.13.jar --server.port=8081 --mappings=mappings