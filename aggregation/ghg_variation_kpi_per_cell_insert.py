# %%
from SPARQLWrapper import SPARQLWrapper, POST
from io import BytesIO
# import pandas as pd
import rdflib

# %%
# Getting data from sparql endpoint
endpoint = SPARQLWrapper("http://127.0.0.1:7200/repositories/USAGE-LD/statements")
query = open('aggregation/ghg_variation_kpi_per_cell_insert.rq', 'r').read() # SameAs inference should be OFF
endpoint.setQuery(query)
endpoint.setMethod(POST)
endpoint.query()
