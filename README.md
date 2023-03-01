# Machine Learning

I'm using this repo to compliment my blog ([briansigafoos.com](https://briansigafoos.com/)) as I explore Machine Learning:

- [fast.ai course](https://course.fast.ai/)
- [Andrej Karpathy's Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

## Setup

## Development

Install Python using [mamba](https://mamba.readthedocs.io). Anywhere you see instructions for `conda`, you can use `mamba` instead (it's faster). Why not `pip`? If you're doing ML, `mamba`/`conda` makes it easier to have everything you need (including Python), and to optimize packages for your GPU.

```shell
# First:
# Install mamba for your machine: https://github.com/conda-forge/miniforge#mambaforge
# Or use this script: https://github.com/fastai/fastsetup/blob/master/setup-conda.sh

# Packages
mamba install -y -c fastchan \
  jupyter \
  ipywidgets \
  notebook \
  numpy \
  pandas \
  pytorch \
  fastai \
  graphviz \
  psycopg2 \
  python-dotenv
```

### Linters

- Install [black](https://github.com/psf/black) `pip install black` + `pip install 'black[jupyter]'`
- Install [pre-commit] `pip install pre-commit` and `pre-commit install; touch .pre-commit-config.yaml`

### Kaggle credentials

From kaggle.com > My Account > Create new API token to download credentials in `kaggle.json`.

```shell
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

## Maintenance

- Update pre-commit hooks using `pre-commit autoupdate`

## TODO

- [x] Add black and configure for VSCode
- [x] Add VSCode tasks to autoformat code
- [x] Add pre-commit hooks
- [x] Add Github Action to run linters
- [x] Add isort to auto-sort imports
