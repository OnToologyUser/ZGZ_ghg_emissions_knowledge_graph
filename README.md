# Zaragoza GHG emissions KG construction pipeline
Batch pipeline scripts that orchestrates multiple tools to construct the Zaragoza GHG emissions Knowledge Graph.

## To run the pipeline script:
1. Clone the current repository.
2. Make sure you have Git and Docker installed.
3. Get the tools needed by running the script `get_tools.sh` within the tools folder.
4. Pip install Python's libraries requirements with the `pip install -r requirements.txt` command.
5. Place raw data following the directory tree: _./data/ZGZ/Sector/raw_ (Raw files names should not include whitespaces)
6. Run the `pipeline.sh` script.
7. As a result you should be able to access to a GraphDB instance with the integrated GHG emissions running in the port `7200`.

## Aggregations:
A set of aggregation queries and scripts are available in the aggregation folder to enrich the knowledge graph. Make sure the triplestore instance is running before executing any of the scripts.
After inserting the aggregated data, the triplestore will contain the integrated GHG emissions at the cell level.

Run the `aggregate.sh` script to get the knowledge graph version at the the district level in the data folder. 

## Tools needed

| Tool                    | Source                                                    |
|-------------------------|-----------------------------------------------------------|
| Chowlk                  | https://github.com/oeg-upm/Chowlk                         |
| GraphDB                 | https://github.com/Ontotext-AD/graphdb-docker             |
| Openrefine batch docker | https://github.com/opencultureconsulting/openrefine-batch |
