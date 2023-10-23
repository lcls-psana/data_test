###!/usr/bin/env python
"""
Usage::
  import data_test.absolute_path as ap
  path = ap.path_to_xtc_test_file(fname='xppn4116_run137_3events.xtc')

Created on 2023-10-23 by Mikhail Dubrovin
"""
import os

#print('XXX __file__', __file__)
#print('XXX lstat', os.lstat(__file__))

path = __file__  # /sdf/home/d/dubrovin/LCLS/con-py3/arch/x86_64-rhel7-gcc48-opt/python/data_test/absolute_path.py@ <<< LINK

if os.path.islink(__file__):
    import pathlib
    path = pathlib.Path(__file__).resolve() # <<< abs path: /sdf/home/d/dubrovin/LCLS/con-py3/data_test/src/absolute_path.py
    #print('XXX link.resolve():', path)

DIR_DATA_TEST = os.path.dirname(path).strip('src')
DIR_XTC_TEST = os.path.join(DIR_DATA_TEST, 'xtc')  # /sdf/home/d/dubrovin/LCLS/con-py3/data_test/xtc/ <<< for test release

#DIR_DATA_TEST = os.path.abspath(os.path.dirname(__file__)).strip('src')
#print('XXX DIR_DATA_TEST', DIR_DATA_TEST)

def path_to_xtc_test_file(fname='xppn4116_run137_3events.xtc'):
    return os.path.join(DIR_XTC_TEST, fname)

if __name__ == '__main__':
    path = path_to_xtc_test_file()
    print('path_to_xtc_test_file: %s' % path\
          + '\nos.path.exists(path): %s' % os.path.exists(path))
# EOF
