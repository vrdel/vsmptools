#!/usr/bin/python

import sys
import subprocess

numactl = "numactl"
numastr = "nodebind"
coresstr = "physcpubind"

def main():
    n_numanodes = 0
    n_cores = 0
    numanodes = list()
    cpus = list()
    coresarg = sys.argv[1]

    out = subprocess.check_output('%s -s' % numactl, shell=True)
    for o in out.split('\n'):
        if o.startswith(numastr):
            numanodes = o.split()[1:]
        if o.startswith(coresstr):
            cpus = o.split()[1:]

    n_numanodes = len(numanodes)
    n_cores = len(cpus)

    cores_per_numa = n_cores / n_numanodes

    i = 0
    j = 0
    numa_to_cores = dict()
    while i < n_numanodes:
        numa_to_cores[i] = list()
        elem_processed = 0
        while j < cpus:
            numa_to_cores[i].append(cpus[j])
            elem_processed += 1
            j += 1
            if elem_processed == cores_per_numa:
                break
        i += 1

    numanodes = set()
    for c in coresarg.split(','):
        for (key, value) in numa_to_cores.iteritems():
            if c in value:
                numanodes.update([key])

    numanode_outstr = ''
    for n in numanodes:
        numanode_outstr += '%s,' % n

    print numanode_outstr[0:-1]

main()
