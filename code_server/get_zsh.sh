#!/bin/bash
# https://kifarunix.com/how-to-install-and-setup-zsh-and-oh-my-zsh-on-ubuntu-18-04/

apt-get update && apt-get upgrade && apt-get install zsh fonts-powerline
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

sed -i "s/\"terminal.integrated.shell.linux.*/\"terminal.integrated.shell.linux\": \"\/usr\/bin\/zsh\"/g" ./code_server/settings.json

if [ -z $1 ]; then
  theme="robbyrussell"
else
  theme=$1
fi
sed -i "s/ZSH_THEME=.*/ZSH_THEME=\"$theme\"/g" ~/.zshrc
