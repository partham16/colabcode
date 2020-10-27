[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/partham16/colabcode)

# ColabCode

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

### Forked from [abhishekkrthakur/colabcode](https://github.com/abhishekkrthakur/colabcode)

## And **Modified**:
#### - Add [`oh-my-bash`](https://github.com/partham16/colabcode/issues/1) pretty prompt

#### - Add [`bash-powerline`](https://github.com/partham16/colabcode/issues/7) theme
![](https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/themes/powerline-plain/powerline-plain-dark.png)

#### - Add **vscode** persistent [`settings.json`](https://github.com/partham16/colabcode/pull/3)

#### - Add bash [`autocomplete`](https://github.com/partham16/colabcode/issues/6)

#### - Add `zsh` and `oh-my-zsh`

#### - Add password randomization

#### - Better *development* support w/ `pre-commit`, `flake8`, `black` etc.

## Installation (run in a [colab](https://colab.research.google.com/notebooks/empty.ipynb) cell):
```bash
%%bash
git clone https://github.com/partham16/colabcode.git
cd /content/colabcode
git checkout zsh
pip install -r requirements.txt
```
And next:

```python
from colabcode.code import ColabCode
ColabCode()
```


## To Be Added:
- Bring your own `settings.json`
- Bring your own **bash / zsh themes**
- Bring your own **list of installs**
