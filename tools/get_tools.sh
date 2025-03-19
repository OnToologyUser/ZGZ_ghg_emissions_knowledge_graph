#!/bin/bash
# Getting Openrefine batch repository and downgrade its version to 2.7 (to support xlsx files)
git clone https://github.com/opencultureconsulting/openrefine-batch.git
sed -i 's|openrefine_URL=.*|openrefine_URL="https://github.com/OpenRefine/OpenRefine/releases/download/2.7/openrefine-linux-2.7.tar.gz"|' openrefine-batch/openrefine-batch.sh

# Getting Chowlk repository and building the docker image (it's not available in docker hub yet)
git clone https://github.com/oeg-upm/Chowlk.git
cd Chowlk
docker build -t chowlk-chowlk:latest .
cd ..

# Getting GraphDB repository 
git clone https://github.com/Ontotext-AD/graphdb-docker.git
cd graphdb-docker
git switch update_the_preload
cd ..