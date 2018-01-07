#!/usr/bin/env bash


[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
rvm use ruby-2.4.0
bundle exec jekyll serve
