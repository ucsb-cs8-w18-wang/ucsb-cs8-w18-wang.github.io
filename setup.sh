#!/usr/bin/env bash

echo "Installing software needed to run Jekyll locally... "

[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"

rvm install ruby-2.4.0
rvm use ruby-2.4.0
gem install bundler
bundle install --path vendor/bundle
echo "Done."
