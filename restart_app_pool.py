#!/usr/bin/python3

import iis_bridge as iis

poolNameList = iis.get_pool_names()

for i in poolNameList:
    if iis.pool.is_running(i) == False:
        iis.pool.restart(i)
