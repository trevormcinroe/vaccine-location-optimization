import os
import sys


class Optimizer:
    def __init__(self):

        self.opt_binary = None

        self._load_opt_binary()

    def _load_opt_binary(self):
        op_sys = sys.platform

        if 'linux' in op_sys:
            self.opt_binary = './bin/Ipopt-3.11.8-linux64mac64win32win64-matlabmexfiles-1/ipopt.m'
        elif 'darwin' in op_sys:
            self.opt_binary = './bin/Ipopt-3.11.1-mac-osx-x86_64-gcc4.5.3/bin/ipopt'
        else:
            self.opt_binary = './bin/Ipopt-3.11.1-win64-intel13.1/bin/ipopt.exe'

