: > ./requirements/requirements.txt
: > ./requirements/requirements-dev.txt
chmod 777 ./requirements/requirements.txt
chmod 777 ./requirements/requirements-dev.txt

docker_container_name="update_deps:local"
docker build -t $docker_container_name .
docker run -v /$PWD:/opt -it $docker_container_name /bin/bash /opt/requirements/install_and_freeze.sh
