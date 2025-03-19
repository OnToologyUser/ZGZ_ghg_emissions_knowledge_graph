# %%
from SPARQLWrapper import SPARQLWrapper2
from io import BytesIO
# import pandas as pd
import rdflib

# %%
# Getting data from sparql endpoint
endpoint = SPARQLWrapper2("http://127.0.0.1:7200/repositories/USAGE-LD")
query = open('aggregation/district_level_kpiaValues_construct.rq', 'r').read() # SameAs inference should be OFF
endpoint.setQuery(query)
qres = endpoint.queryAndConvert()
# Convert results to pandas dataframe
# print(f"Total bindings: {len(qres.bindings)}")
# # qres_csv = qres.serialize(format="csv")
# df =pd.json_normalize(qres.fullResult["results"]["bindings"])
# # df = pd.read_csv(BytesIO(qres_csv))
# df
# %%
res_graph=rdflib.Graph()
res_graph.parse(qres)
res_graph.serialize(destination="data/ZGZ/district_level_kpiaValues_construct.nt", format="nt")

# %%
