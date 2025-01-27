#### createProbablePrime()


 static BigInteger Primes::createProbablePrime ( int bitLength, int certainty, const int \* randomSeeds = nullptr, int numRandomSeeds = 0 ) static 
 

Creates a random prime number with a given bitlength.The certainty parameter specifies how many iterations to use when testing for primality. A safe value might be anything over about 2030.The randomSeeds parameter lets you optionally pass it a set of values with which to seed the random number generation, improving the security of the keys generated.