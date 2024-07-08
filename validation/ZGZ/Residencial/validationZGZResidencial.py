# %%
from maplib import Mapping
import time

# %%
m = Mapping()
shape_graph = "urn:eu:shacl"
m.read_triples("validation/ZGZ/Residencial/shapesZGZResidencial.ttl", graph=shape_graph)
load_tic = time.time()
m.read_triples("data/rdf-file.ttl")
load_tictoc = time.time() - load_tic

tic = time.time()
report = m.validate(shape_graph=shape_graph)
tictoc = time.time() - tic

df = report.report
print("Load estimated time: ", load_tictoc, "\nValidation estimated time: ", tictoc)
print(df)
# %%
