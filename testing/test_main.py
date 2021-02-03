try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) : 
        inputs, outputs = [], []
        for i in range(50) :
            val = np.random.uniform(-2,2)
            inputs.append((val,))
            vv = np.zeros(10)
            val = val - np.floor( val ) 
            for j in range(10) : 
                ppp = 10**(-1-j)
                vv[j] = np.floor( val / ppp )
                val = val - vv[j]*ppp
            outputs.append(vv)
        assert( fc.check_func( 'getDecimalDigits', inputs, outputs ) )
