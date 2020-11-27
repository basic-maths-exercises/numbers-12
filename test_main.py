import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) : 
        for i in range(50) :
            val = np.random.uniform(-2,2)
            arr = getDecimalDigits(val)
            vv = int(np.floor( val / 1 ))
            val = val - vv 
            for j in range(4) : 
                ppp = 10**(-1-j)
                vv = int(np.floor( val / ppp ) )
                val = val - vv*ppp
                self.assertTrue( vv==arr[j], "Your function is not working" )
