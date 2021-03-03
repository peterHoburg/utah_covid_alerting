FROM python@sha256:e2cd43d291bbd21bed01bcceb5c0a8d8c50a9cef319a7b5c5ff6f85232e82021

RUN adduser --system --group --shell /bin/sh default \
 && mkdir /home/default/bin
USER default

WORKDIR /opt
ENV PYTHONPATH $PYTHONPATH:/opt:/home/default/.local/bin
ENV PATH $PATH:/home/default/.local/bin

COPY ["./requirements/requirements.txt", "./requirements/requirements.txt"]
RUN pip install --user -r ./requirements/requirements.txt

# This is only availiable during a docker build to have them persist into a docker run use ENV
ARG DEV=false

# This can not be set in a docker build. Using the -e in a docker run will change these during runtime
ENV DEV="${DEV}"

# This allows you to install dev dependencies in a docker layer negating the need to install them
#   every time a container is run.
# WARNING: This script uses the ARG/ENV DEV value to decide if the requirements-dev.txt should be installed
COPY ["./requirements/requirements-dev.txt", "./requirements/requirements-dev.txt"]
COPY ["./requirements/install_dev_requirements.sh", "./requirements/install_dev_requirements.sh"]
RUN bash ./requirements/install_dev_requirements.sh
RUN pip check

# These are only availiable during a docker build to have them persist into a docker run use ENV
ARG ENVIRONMENT=local
ARG DEBUG=false

# These can not be set in a docker build. Using the -e in a docker run will change these during runtime
ENV ENVIRONMENT="${ENVIRONMENT}"
ENV DEBUG="${DEBUG}"


# Always have this as far down as you can. If anything being coppied in this step changes all steps
#   run after it will be rerun instead of using existing container layers.
ADD . /opt

# This is executed during docker run. This is a good place to set DB and other secrets to env vars
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

# This is the last thing docker runs. You can overwrite it like so:
#   docker run -it <docker_container_name:tag> <command_to_run IE /bin/bash>
CMD ["python", "python_docker_example/main.py"]
