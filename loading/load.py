# %%
# ### Import libraries block
import zipfile
import time
import rdflib
from io import BytesIO
import pandas as pd
# from pyshacl import validate

# %%
# ### Data parsing block
# Parse rdf test data to rdflib graph 

g = rdflib.Graph()
with open("../data/rdf-file.nt", "r", encoding="utf-8") as file:
    g.parse(data=file.read(), format="nt")

print(f"Number of data statements parsed: {len(g)}")

# %% SPARQL query block
# Set query and get results as dataframe

query = """
PREFIX s4city: <https://saref.etsi.org/saref4city/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX bigg: <http://bigg-project.eu/ld/ontology#>
PREFIX vcard: <http://www.w3.org/2006/vcard/ns#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>

SELECT ?cell # ?wkt (count(DISTINCT ?feature) as ?wktLabel) 
WHERE{
  ?feature a geo:Feature;
           geo:hasGeometry/geo:asWKT ?cell.
    FILTER (geof:sfWithin(?cell, "POLYGON((-0.8804512023925781 41.658036243288706,-0.8836483955383301 41.654573331595515,-0.8798933029174806 41.652633378403664,-0.8760738372802735 41.65657735411503,-0.8804512023925781 41.658036243288706))"^^geo:wktLiteral))
#   FILTER (geof:sfWithin(?cell,?wkt ))
#   {
#   select * where { 
    #   ?s a s4city:Neighbourhood;
    #   geo:hasGeometry/geo:asWKT ?wkt.
#   }
#   }
} #GROUP BY ?wkt
"""
qres = g.query(query)

# Convert results to pandas dataframe
print(f"Total bindings: {len(qres.bindings)}")
qres_csv = qres.serialize(format="csv")
df = pd.read_csv(BytesIO(qres_csv))
df
# %%
