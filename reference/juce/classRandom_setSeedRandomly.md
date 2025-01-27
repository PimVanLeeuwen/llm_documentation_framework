#### setSeedRandomly()


 void Random::setSeedRandomly ( ) 
 

Reseeds this generator using a value generated from various semirandom system properties like the current time, etc.Because this function convolves the time with the last seed value, calling it repeatedly will increase the randomness of the final result.