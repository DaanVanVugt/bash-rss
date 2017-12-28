#!/bin/sh
wget http://bash.org?latest
cat 'index.html?latest' | python bashlatest.py > ../.html/bash.org_latest.rss 
rm index.html\?latest*
