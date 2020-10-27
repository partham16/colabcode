#!/bin/bash

# bash strict mode  ## ERROR
# set -eu

if [ -z $1 ]; then
  theme="powerline-plain"
else
  theme=$1
fi

if [ "$theme" = "powerline-undu" ]; then
  echo "source ~/.powerline.bash" >> ~/.bashrc
else
  # -i : inplace, s/ : substitution, /g : global
  # https://stackoverflow.com/a/748586/13070032
  # sed 's/foo/$BAR/g' doesn't work, but sed "s/foo/$BAR/g" DOES
  # \" : escape -> adds " outside $theme
  sed -i "s/OSH_THEME=.*/OSH_THEME=\"$theme\"/g" ~/.bashrc
fi

# echo "$theme"
# echo $(grep "OSH_THEME=" ~/.bashrc)
