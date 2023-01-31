# Machine Learning

I'm using this repo to compliment my blog ([briansigafoos.com](https://briansigafoos.com/)) as I explore Machine Learning:

- [fast.ai course](https://course.fast.ai/)
- [Andrej Karpathy's Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

## Setup

### Development

```
mamba install -y \
  diffusers \
  transformers \
  black
```

### Kaggle credentials

From kaggle.com > My Account > Create new API token to download credentials in `kaggle.json`.

```shell
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

### Linters

- Install [black](https://github.com/psf/black) `pip install black` + `pip install 'black[jupyter]'`
- Install [pre-commit] `pip install pre-commit` and `pre-commit install; touch .pre-commit-config.yaml`

## Maintenance

- Update pre-commit hooks using `pre-commit autoupdate`

## TODO

- [x] Add black and configure for VSCode
- [x] Add VSCode tasks to autoformat code
- [x] Add pre-commit hooks
- [x] Add Github Action to run linters
- [x] Add isort to auto-sort imports
