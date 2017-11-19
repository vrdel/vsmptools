# vsmptools
Small tools used in job description scripts for ScaleMP system of Isabella cluster

* `cores_to_numa.py` - used with `numactl` tool for pinning files to specific NUMA nodes/domain that will be constructed from given free CPU cores
* `randvsmp.py` - better randomness used for backoff of two jobs submitted at same time 
