#!/bin/bash

## aggregation
python3 aggregation/ghg_kpi_per_cell_insert.py
python3 aggregation/ghg_variation_kpi_per_cell_insert.py

# make sure the previous generated triples are inserted in the triplestore before aggregating at the district level
python3 aggregation/district_level_kpiaValues_insert.py 

# construct the district level graph in the data folder
python3 aggregation/construct_district_level_ZGZ_graph.py