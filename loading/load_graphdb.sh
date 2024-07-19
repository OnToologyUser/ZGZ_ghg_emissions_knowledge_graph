cp loading/graphdb-repo-config.ttl tools/graphdb-docker/preload/graphdb-repo.ttl
cp data/rdf-file.zip tools/graphdb-docker/preload/import/
cd tools/graphdb-docker/preload/
docker-compose build #--no-cache --force-rm
docker-compose up -d #-d --build --force-recreate
