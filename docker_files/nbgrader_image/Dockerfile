FROM phaustin/base:may19

#
# bind mount these folders
#

RUN mkdir -p ${HOME}/work/data_share
RUN mkdir -p ${HOME}/work/source
RUN mkdir -p ${HOME}/work/release
RUN mkdir -p ${HOME}/work/submitted
RUN mkdir -p ${HOME}/work/exchange

RUN chown -R jovyan ${HOME}
RUN chgrp -R jovyan ${HOME}

COPY jupyter_notebook_config.py /etc/jupyter/

USER ${NB_USER}

RUN echo "move nbgrader files" \
  && mv ${HOME}/nbgrader_files/* /home/jovyan/work/ 

RUN echo "cleanup root directory" \
  && rm -rf Dockerfile autotest_files environment.yml nbgrader_files \
  && rm -rf apt.txt conda-linux-64.lock  jupyter_notebook_config.py  postBuild 

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc

WORKDIR "${HOME}/work"


RUN touch version_nbgrader_may_19.txt

CMD ["jupyter", "notebook"]
