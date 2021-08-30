# Based version
Autotest supports nbgrader version [0.6.2](https://pypi.org/project/nbgrader/)
# Setup
1. Create a python virtual enviroment:
  * Python [venv](https://docs.python.org/3/tutorial/venv.html)
  * [Anaconda](https://www.anaconda.com/)
2. Install the current version of nbgrader:
  ```bash
  pip install nbgrader
  ```
  
Or, if you use [Anaconda](https://www.anaconda.com/)

  ```bash
  conda install jupyter
  conda install -c conda-forge nbgrader
  ```
3. Activate this virtual enviroment
4. Clone this repository to local
5. Execute `./install_autotest.sh` under the root of this repository, it will automatically install `autotest generation` module over the nbgrader package
