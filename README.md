# Machine Learning

## Setup kaggle

From kaggle.com > My Account > Create new API token to download credentials in `kaggle.json`.

```shell
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

## Linters

- Install [black](https://github.com/psf/black) `pip install black` + `pip install 'black[jupyter]'`
- Install [pre-commit] `pip install pre-commit` and `pre-commit install`

## Maintenance

- Update pre-commit hooks using `pre-commit autoupdate`

## TODO

- [x] Add black and configure for VSCode
- [x] Add VSCode tasks to autoformat code
- [x] Add pre-commit hooks
- [ ] Add Github Action to run linters
