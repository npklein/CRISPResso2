#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
CRISPResso2 - Kendell Clement and Luca Pinello 2018
Software pipeline for the analysis of genome editing outcomes from deep sequencing data
(c) 2018 The General Hospital Corporation. All Rights Reserved.
'''

import os
import subprocess as sb
import sys
usage = '\n- CRISPResso2 Docker Container -\n\t- Possible commands: \n\t  CRISPResso\n\t  CRISPRessoBatch\n\t  CRISPRessoPooled\n\t  CRISPRessoWGS\n\t  CRISPRessoCompare\n\t  CRISPRessoPooledWGSCompare\n\t  CRISPRessoAggregate\n\t  License\n\t- this docker version should be run like this:\n\tdocker run -v ${PWD}:/DATA -w /DATA -i pinellolab/crispresso2 CRISPResso -r1 fastq1.fq -a AAAATTT \n'

if len(sys.argv)==1:

    print(usage)
    sys.exit(1)

if sys.argv[1]=='CRISPResso':
    sb.call(["CRISPResso"]+ sys.argv[2:])
elif sys.argv[1]=='CRISPRessoBatch':
    sb.call(["CRISPRessoBatch"]+ sys.argv[2:])
elif sys.argv[1]=='CRISPRessoCompare':
    sb.call(["CRISPRessoCompare"]+ sys.argv[2:])
elif sys.argv[1]=='CRISPRessoPooled':
    sb.call(["CRISPRessoPooled"]+ sys.argv[2:])
elif sys.argv[1]=='CRISPRessoPooledStep1':
    sb.call(["CRISPRessoPooledStep1"]+ sys.argv[2:])
elif sys.argv[1]=='CRISPRessoPooledStep2':
    sb.call(["CRISPRessoPooledStep2"]+ sys.argv[2:])
elif sys.argv[1]=='CRISPRessoWGS':
    sb.call(["CRISPRessoWGS"]+ sys.argv[2:])
elif sys.argv[1]=='CRISPRessoPooledWGSCompare':
    sb.call(["CRISPRessoPooledWGSCompare"]+ sys.argv[2:])
elif sys.argv[1]=='CRISPRessoAggregate':
    sb.call(["CRISPRessoAggregate"]+ sys.argv[2:])
elif sys.argv[1]=='License':
    with open("LICENSE.txt", 'r') as fin:
        print(fin.read())
else:
    print(usage)
