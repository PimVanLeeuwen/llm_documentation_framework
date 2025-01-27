#### createKeyPair()


 static void RSAKey::createKeyPair ( RSAKey & publicKey, RSAKey & privateKey, int numBits, const int \* randomSeeds = nullptr, int numRandomSeeds = 0 ) static 
 

Creates a public/private keypair.Each key will perform oneway encryption that can only be reversed by using the other key.The numBits parameter specifies the size of key, e.g. 128, 256, 512 bit. Bigger sizes are more secure, but this method will take longer to execute.The randomSeeds parameter lets you optionally pass it a set of values with which to seed the random number generation, improving the security of the keys generated. If you supply these, make sure you provide more than 2 values, and the more your provide, the better the security.

Member Data Documentation