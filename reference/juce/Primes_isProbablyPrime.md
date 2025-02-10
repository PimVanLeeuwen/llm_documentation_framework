#### isProbablyPrime()


 static bool Primes::isProbablyPrime ( const BigInteger & number, int certainty ) static 
 

Tests a number to see if it's prime.This isn't a bulletproof test, it uses a MillerRabin test to determine whether the number is prime.The certainty parameter specifies how many iterations to use when testing a safe value might be anything over about 2030.