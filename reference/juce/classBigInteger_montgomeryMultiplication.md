#### montgomeryMultiplication()


 void BigInteger::montgomeryMultiplication ( const BigInteger & other, 
 
 const BigInteger & modulus, 
 const BigInteger & modulusp, 
 int k ) 

Performs the Montgomery Multiplication with modulo.This object is left containing the result value: ((this \* other) \* R1) % modulus. To get this result, we need modulus, modulusp and k such as R = 2^k, with modulus \* modulusp R \* R1 = GCD(modulus, R) = 1