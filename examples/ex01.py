#!/usr/bin/env python

import os
DIR_DATA_TEST = os.path.abspath(os.path.dirname(__file__)).strip('examples')
DIR_XTC_TEST = os.path.join(DIR_DATA_TEST, 'xtc')

from psana import Detector, DataSource
fname = os.path.join(DIR_XTC_TEST, 'xppn4116_run137_3events.xtc')
print('fname: %s' % fname)

from Detector.GlobalUtils import info_ndarr
ds = DataSource(fname)
det = Detector('XppEndstation.0:Opal1000.1') # 'XppGon.0:Epix100a.1'
for i, evt in enumerate(ds.events()):
    if i<1:
      print('\nevt.keys():')
      for k in evt.keys():
        print(str(k))
      print('\ndet.raw(evt) for %s:' % det.name) # det.source
    print(info_ndarr(det.raw(evt),'Ev#%d:' % i))
    #print(dir(det))

# EOF
