# EC2 Image

Austin Privett
12/3/2018

My workflow for the creation of the EC2 image. [Track GitHub Issue.](https://github.com/dhplabs/data-science/issues/6)

## 1. Get conda package manager

Download [miniconda](https://conda.io/miniconda.html) and send  across via
scp. Installation instructions
[here](https://conda.io/docs/user-guide/install/linux.html); what I did on EC2
is copied below.

```bash
# from client laptop
scp -i <publickey> <name>@<server>:/vol/.downloads
# from EC2 instance
ssh -i <publickey> <name>@<server>
cd /vol/.downloads
bash Miniconda3-latest-Linux-x86_64.sh # follow instructions
exit # to get new nev
# log back in via ssh
ssh -i <publickey> <name>@<server>
conda update conda
```

## 2. Get JupyterLab + BeakerX via conda.

Instructions [here](https://github.com/twosigma/beakerx) and
[here](https://github.com/twosigma/beakerx#build-and-install-for-jupyter-lab).
I suggest you only use BeakerX for SQL and pandas work, then use JupyterLab or
Jupyter for the remaining ML + Viz work, as there seem to be conflicts between
BeakerX and JupyterLab (and BeakerX is pretty heavy).

```bash
# Set up JupyterLab (let's just stick with JupyterLab unless we can't)
conda create -y -n labx 'python>=3' nodejs pandas 'openjdk=8.0.121' maven py4j requests sqlalchemy
source activate labx
conda config --env --add pinned_packages 'openjdk=8.0.121'
conda install -y -c conda-forge jupyterlab beakerx nodejs sqlalchemy-redshift
beakerx install
jupyter labextension install @jupyter-widgets/jupyterlab-manager beakerx-jupyterlab

# Set up Jupyter (old notebook)
conda create -y -n beakerx 'python>=3' nodejs pandas 'openjdk=8.0.121' maven py4j requests sqlalchemy
source activate beakerx
conda config --env --add pinned_packages 'openjdk=8.0.121'
conda install -y -c conda-forge ipywidgets beakerx sqlalchemy-redshift
beakerx install
```

## 3. Plotting packages

BeakerX contains some plotting capabilities (I haven't used them, yet), but
below is the environment I'm supporting. Note that plotly has some nice
features, but is missing datashading compatibility, so I'm not worrying
about supporting it yet.

```bash
conda create -y -n pyvizlab 'python>=3'
source activate pyvizlab
conda install -y -c conda-forge jupyterlab category_encoders scikit-learn pandas numba sqlalchemy sqlalchemy-redshift umap-learn
conda install -y -c pyviz/label/dev pyviz
# conda install -c plotly plotly # skipping this for now

# my version of umap is different, but I want all the dependencies
# maybe try to get this going without conda

# some neat extensions (batteries included)
jupyter labextension install @jupyter-widgets/jupyterlab-manager
   # allows for live plotting of bokeh et al
   @pyviz/jupyterlab_pyviz \
   # table of contents panel
   @jupyterlab/toc \
   # data visualization
   jupyterlab_voyager

jupyter labextension install @jupyter-widgets/jupyterlab-manager @pyviz/jupyterlab_pyviz @jupyterlab/toc jupyterlab_voyager

# and the vanillya jupyter version
conda create -y -n pyviz 'python>=3'
source activate pyviz
conda install -y -c conda-forge jupyter ipywidgets category_encoders scikit-learn pandas numba sqlalchemy sqlalchemy-redshift
conda install -y -c pyviz/label/dev pyviz
```

## 3. Get ML Packages via conda.

## 4. Get DHP Packages via git or scp.

## 5. See available environments:

```bash
(pyviz) [aprivett@ip-10-20-0-172 ~]$ conda env list
# conda environments:
#
base                     /vol/labenv/miniconda3
beakerx                  /vol/labenv/miniconda3/envs/beakerx
labx                     /vol/labenv/miniconda3/envs/labx
pyviz                 *  /vol/labenv/miniconda3/envs/pyviz
pyvizlab                 /vol/labenv/miniconda3/envs/pyvizlab
```

After this point, know that you have space in your home directory `~` and
the python software is loaded to `/vol/dhplabs`
