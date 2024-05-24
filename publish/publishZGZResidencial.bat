copy "..\data\ZGZ\Residencial\rdf\ZGZ-residencial-output-01-BBDD-EnerEst-EResidenciales-2021-v001-refined.nt" "../tools/Helio/mappings/data/rdf-file.nt"
cd "../tools/Helio"
java -jar publisher-0.3.13.jar --server.port=8080 --mappings=mappings