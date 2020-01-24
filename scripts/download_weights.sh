#!/bin/bash

wget -c --tries=0 --read-timeout=20 https://github.com/jimmy-academia/downloadable/releases/download/weight.cyc-pix/pre.tar.gz
wget -c --tries=0 --read-timeout=20  https://github.com/jimmy-academia/downloadable/releases/download/weight.cyc-pix/prehd.tar.gz

tar -xzvf pre.tar.gz    # pretrained_weights/ smile blond bald glass pix_black_masked pix_masked_black
tar -xzvf prehd.tar.gz  # prehd/ black_masked masked_blond 
rm pre.tar.gz prehd.tar.gz

mv prehd/black_masked pretrained_weights/pixhd_black_masked
mv prehd/masked_blond pretrained_weights/pixhd_masked_blond
mv pretrained_weights weights
rm -d prehd
