#!/usr/bin/env zsh
ruby -rnet/http -e "Net::HTTP.get(URI('https://rubygems.org'))"