# docker iamge for autotest/nbgrader

* framework based on https://github.com/pangeo-data/pangeo-docker-images

* all security (password/token) turned off -- use on on localhost or behind a proxy

* to build:

       docker-compose up

  which will build phaustin/baae and phaustin/nbgrader
  and launch a notebook server on localhost:8888

