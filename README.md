# Based version
Autotest supports nbgrader version [0.6.2](https://pypi.org/project/nbgrader/)
# Setup
1. Create a python virtual environment:
  * Python [venv](https://docs.python.org/3/tutorial/venv.html)
  * [Anaconda](https://www.anaconda.com/)
2. Activate this virtual environment
3. Clone this repository to local
4. Install the requirements:
  ```bash
  pip install -r reqs.txt 
  ```
5. Execute `./install_autotest.sh` under the root of this repository, it will automatically install `autotest generation` module over the nbgrader package
6. Install extensions
  ```bash
    jupyter nbextension install --sys-prefix --py nbgrader --overwrite
    jupyter nbextension enable --sys-prefix --py nbgrader
    jupyter serverextension enable --sys-prefix --py nbgrader
  ```
