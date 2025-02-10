#### extendedEuclidean()


 void BigInteger::extendedEuclidean ( const BigInteger & a, 
 
 const BigInteger & b, 
 BigInteger & xOut, 
 BigInteger & yOut ) 

Performs the Extended Euclidean algorithm.This method will set the xOut and yOut arguments such that (a \* xOut) (b \* yOut) = GCD (a, b). On return, this object is left containing the value of the GCD.