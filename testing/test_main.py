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
            vv = np.zeros(5)
            vv[0] = np.floor( val / 1 )
            val = val - vv[0] 
            for j in range(4) : 
                ppp = 10**(-1-j)
                vv[j+1] = np.floor( val / ppp )
                val = val - vv[j+1]*ppp
            outputs.append(vv)
            assert( fc.check_func( 'getDecimalDigits', inputs, outputs ) )
