# docker image for autotest/nbgrader

* framework based on 2-stage conda-lock https://github.com/pangeo-data/pangeo-docker-images

* all security (password/token) turned off -- use on localhost or behind a proxy

* to build:

       docker-compose up

  which will build phaustin/base and phaustin/nbgrader
  and launch a notebook server on localhost:8888

