FROM ubuntu:20.04

# Adapted from https://github.com/pangeo-data/pangeo-docker-images

# SEE: https://github.com/phusion/baseimage-docker/issues/58
ARG DEBIAN_FRONTEND=noninteractive

# set up environment variables
ENV CONDA_VERSION=4.10.3-2 \
    CONDA_ENV=notebook \
    NB_USER=jovyan \
    NB_UID=1002 \
    NB_GID=1004 \
    SHELL=/bin/bash \
    LANG=C.UTF-8  \
    LC_ALL=C.UTF-8 \
    CONDA_DIR=/srv/conda

ENV NB_PYTHON_PREFIX=${CONDA_DIR}/envs/${CONDA_ENV} \
    HOME=/home/${NB_USER} \
    PATH=${CONDA_DIR}/bin:${PATH}

# Create jovyan user, home folder, subfolders, set up permissions
RUN echo "Creating ${NB_USER} user and home folder structure..." \
    && groupadd --gid ${NB_GID} ${NB_USER}  \
    && useradd --create-home --gid ${NB_GID} --no-log-init --uid ${NB_UID} ${NB_USER} \
    && chown -R ${NB_USER}:${NB_USER} /srv
    && mkdir -p ${HOME}/course/source \
    && mkdir -p ${HOME}/course/release \
    && chown -R ${NB_USER}:${NB_USER} ${HOME}

RUN echo "Installing basic apt-get packages..." \
    && apt-get update --fix-missing \
    && apt-get install -y apt-utils 2> /dev/null \
    && apt-get install -y wget zip tzdata \
    && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN echo "Copying bashrc_conda.txt and condarc.yml into the image" 
COPY --chown=jovyan:jovyan bashrc_conda.txt /tmp
COPY --chown=jovyan:jovyan condarc.yml /srv

RUN echo "Adding conda environment to /etc/profile.d and /home/jovyan/.bashrc" \
    && cat /tmp/bashrc_conda.txt >> /etc/profile.d/init_conda.sh \
    && cat /tmp/bashrc_conda.txt >> ${HOME}/.bashrc \
    && rm /tmp/bashrc_conda.txt \
    
RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc

RUN echo "Moving jupyter notebook config to /etc/jupyter" \
RUN mkdir -p /etc/jupyter
COPY jupyter_notebook_config.py /etc/jupyter

RUN echo "Moving nbgrader_config.py and tests.yml into home/course"
COPY --chown ${NB_USER}:${NB_USER} nbgrader_config.py ${HOME}/course
COPY --chown ${NB_USER}:${NB_USER} tests.yml ${HOME}/course

# Switch to jovyan user
USER ${NB_USER}
WORKDIR ${HOME}

# install miniforge
RUN echo "Installing Miniforge..." \
    && URL="https://github.com/conda-forge/miniforge/releases/download/${CONDA_VERSION}/Miniforge3-${CONDA_VERSION}-Linux-x86_64.sh" \
    && wget --quiet ${URL} -O miniconda.sh \
    && /bin/bash miniconda.sh -u -b -p ${CONDA_DIR} \
    && rm miniconda.sh \
    && conda install -y -c conda-forge mamba bokeh \
    && mamba clean -afy \
    && find ${CONDA_DIR} -follow -type f -name '*.a' -delete \
    && find ${CONDA_DIR} -follow -type f -name '*.pyc' -delete

# Create "notebook" conda environment
RUN echo "Copying conda-linux-64.lock into homedir..."
COPY conda-linux-64.lock ${HOME}
RUN echo "Creating environment from conda-linux-64.lock..." \
    && mamba create --name ${CONDA_ENV} --file conda-linux-64.lock \
    && mamba clean -yaf \
    && find ${CONDA_DIR} -follow -type f -name '*.a' -delete \
    && find ${CONDA_DIR} -follow -type f -name '*.pyc' -delete \
    && rm conda-linux-64.lock

# Install pip packages
# remove cache https://github.com/pypa/pip/pull/6391 ?
COPY requirements.txt ${HOME}
RUN echo "Installing python packages using pip from requirements.txt..." \
    && ${NB_PYTHON_PREFIX}/bin/pip install --no-cache-dir -r requirements.txt

RUN echo "Installing/enabling nbgrader extensions..." \
    && jupyter nbextension install --sys-prefix --py nbgrader --overwrite
    && jupyter nbextension enable --sys-prefix --py nbgrader
    && jupyter serverextension enable --sys-prefix --py nbgrader
    && rm requirements.txt

#RUN echo "Installing autotest..." \
#    && 
#
#cd ${HOME}/autotest_files
#./install_autotest.sh
#echo "ran install_autotest.sh in postbuild"
#
#RUN echo "move nbgrader files" \
#  && mv ${HOME}/nbgrader_files/* /home/jovyan/work/ 
#
#CMD ["jupyter", "notebook"]
#
## finally expose port 8888 for jupyter notebook
#EXPOSE 8888
#
#
