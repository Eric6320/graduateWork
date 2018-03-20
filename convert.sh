#!/bin/tcsh
unset noclobber

set INPUTFILE = $1
set OUTPUTFILE = $2

sed -e "s/;//g; s/ {/:/g; s/}//g; s/{/:/g; s/}//g; s/\/\/\*/#/g; s/\/\//#/g; s/double //g; s/int //g; s/const //g; s/main()://g; s/fabs/abs/g" $INPUTFILE >! $OUTPUTFILE

gedit $OUTPUTFILE
