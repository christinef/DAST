#!/bin/bash
SRC_DIR="./js_src"
for f in $(find $SRC_DIR -type f)
do 
  basename $f
  java -jar ./closure-compiler/compiler.jar --js $f --js_output_file ./js_obfus/$(basename $f).js
done
