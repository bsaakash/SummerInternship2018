# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-3 replay file
# Internal Version: 2013_10_09-07.28.52 126623
# Run by gkim68 on Fri Jul 13 12:01:04 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.13104, 1.1263), width=166.489, 
    height=111.729)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('run_job_script.py', __main__.__dict__)
#: ABAQUS Error: Abaqus/Analysis exited with error.
#* Abaqus/Analysis exited with error.
