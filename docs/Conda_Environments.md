## Setup
This project uses an Conda environment to manage dependencies. The dependencies are recorded in the `environment.yml` file at the base of the repository. The following commands should be executed in the Anaconda Prompt.

* To set up the environment:
```
conda env create -f environment.yml
```
* To activate the Conda environment:
```
conda activate athena
```
* To deactivate the Conda environment:
```
conda deactivate
```
* To remove the Conda environment:
```
conda remove --name athena --all
```

## Contributing
* After installing new packages, save them to the `environment.yml` file:
```
conda env export > environment.yml
```
* To update your environment to reflect new dependencies:
```
conda env update --prefix ./env --file environment.yml  --prune
```
