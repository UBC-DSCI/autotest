<img src="docs/autotest.png" width="450"/> 

Autotest is an extension to [NbGrader](https://github.com/jupyter/nbgrader) that 
automatically generates test code for autograded questions.

You can either set up Autotest on your own machine, or run our demo 
in a docker container.

# Demo
To run the demo, clone this repository and navigate to it.
Give read/write permissions to the `demo/source` and `demo/release` folders
(which will appear in the running docker container's home folder):
```
chmod a+rwx demo/source
chmod a+rwx demo/release
```

Next make sure Docker is installed on your machine, and run in the repository root:
```
docker-compose up
```
This will build a docker image, bind mount the `demo/source` and `demo/release` folders,
and start a Jupyter notebook server. Open your browser and navigate to `localhost:8888`; 
this should open the Jupyter notebook interface.

We have included a few example autograded notebooks in this demo container.
For example, to test Autotest, you can process the `ps3` assignment.
Open a terminal in the Jupyter notebook home folder and run
```
nbgrader generate_assignment --force ps3
```
To see how Autotest processes your questions, run with debug flags:
```
nbgrader generate_assignment --force --debug ps3
```
See the `source/` folder for other demo assignments. You can also add your own in the `demo/source/` folder 
of this repository. Make sure to give `a+rwx` permissions to each assignment you add to the folder, 
as otherwise the jupyter user won't be able to read/write to them.

# Installation
1. Create a python virtual environment:
  * Python [venv](https://docs.python.org/3/tutorial/venv.html)
  * [Anaconda](https://www.anaconda.com/)
2. Activate this virtual environment
3. Clone this repository to local
4. Install the requirements:
  ```bash
  pip install -r requirements.txt 
  ```
5. Execute `./install_autotest.sh` under the root of this repository, it will automatically install `autotest generation` module over the nbgrader package
6. Install extensions
  ```bash
    jupyter nbextension install --sys-prefix --py nbgrader --overwrite
    jupyter nbextension enable --sys-prefix --py nbgrader
    jupyter serverextension enable --sys-prefix --py nbgrader
  ```

# Repository Status
Autotest currently supports NbGrader version [0.6.2](https://pypi.org/project/nbgrader/).
An updated version of Autotest for the newest version of NbGrader is under development.
