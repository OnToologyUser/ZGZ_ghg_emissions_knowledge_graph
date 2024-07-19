# %%
import zipfile
with zipfile.ZipFile('data/rdf-file.zip', 'w') as myzip:
    myzip.write("data/rdf-file.nq",arcname="rdf-file.nq")
    myzip.write("data/rdf-file.nt",arcname="rdf-file.nt")
    myzip.write("ontology/usage_ontology.ttl",arcname="usage-ontology.ttl") 

# %%
