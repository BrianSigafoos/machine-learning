# Machine Learning

## Setup kaggle

From kaggle.com > My Account > Create new API token to download credentials in `kaggle.json`.

```shell
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

## Linters

- Install [black](https://github.com/psf/black) `pip install black` + `pip install 'black[jupyter]'`

## TODO

- [x] Add black and configure for VSCode
- [x] Add VSCode tasks to autoformat code
- [ ] Add Github Action to run linters
