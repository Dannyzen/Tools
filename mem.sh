#!/bin/bash
while true
do
        ps -p $1 -o %cpu,%mem,rss,etime | tee -a $1_mem
        sleep 2
done
