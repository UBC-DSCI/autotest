<img src="docs/autotest.png" width="450"/> 

## [NbGrader](https://github.com/jupyter/nbgrader) extension for automatically generating test code.

![autotest_demo](https://user-images.githubusercontent.com/5981307/170394669-37f7f22b-00fd-441d-9a5e-f82761835f89.gif)


# Demo
To run the demo, make sure Docker is installed on your machine, and run the following
in the root folder of the repository:
```
docker-compose up -d
```
This will build a docker image, bind mount the `demo/source` and `demo/release` folders,
and start a Jupyter notebook server. Open your browser and navigate to `localhost:8888`; 
this should open the Jupyter notebook interface.

> When you are done working, type `docker-compose down` to remove the dangling container.

You will likely need to give read/write permissions to the `demo/source` and `demo/release` folders
(so that the `jupyter` user inside the docker container can read/write to them).
Again in the root folder of the repository, run:
```
chmod a+rwx demo/source
chmod a+rwx demo/release
```

We have included a few example autograded notebooks in this demo container.
For example, you can use Autotest to process the `ps3` assignment.
In the Jupyter notebook interface in your browser, open a terminal (`New -> Terminal`)
and type:
```
nbgrader generate_assignment --force ps3
```
To see how Autotest processes your questions, you can instead run with debug flags:
```
nbgrader generate_assignment --force --debug ps3
```
The release version of the assignment will appear with generated test code in the `release/` folder.

See the `source/` folder for other demo assignments. You can also add your own in the `demo/source/` folder 
of this repository. Make sure to give `a+rwx` permissions to each assignment you add to the folder, 
as otherwise the jupyter user won't be able to read/write to them.

# How It Works

You can [watch a brief explainer video here.](https://youtu.be/chdqmuul_0M) More technical details will be added here in the README soon.

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
