#! /bin/sh
echo "Starting Test plugin installation procedure"
if [ -z "$DIP_HOME" ]
then
	echo "Missing DIP_HOME"
	exit 1
fi
detectedDistrib=$($DKUINSTALLDIR/scripts/_find-distrib.sh)
distrib=`echo "$detectedDistrib"|cut -d ' ' -f 1`
echo "$distrib"
echo "Done"

python2 setup.py install
#$DIP_HOME/bin/python setup.py
#$DIP_HOME/bin/python "print(1)"
#$DIP_HOME/bin/python setup.py install
