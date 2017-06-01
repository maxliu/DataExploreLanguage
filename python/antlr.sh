#!/bin/bash

java -jar ../../../antlr-4.6-complete.jar -o ./base/  -visitor -Dlanguage=Python2 -long-messages ../antlr/de.g4 
