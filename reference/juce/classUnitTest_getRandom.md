#### getRandom()


 Random UnitTest::getRandom ( ) const 
 

Returns a shared RNG that all unit tests should use.If a test needs random numbers, it's important that when an error is found, the exact circumstances can be recreated in order to retest the problem, by repeating the test with the same random seed value. To make this possible, the UnitTestRunner class creates a master seed value for the run, writes this number to the log, and then this method returns a Random object based on that seed. All tests should only use this method to create any Random objects that they need.Note that this method will return an identical object each time it's called for a given run, so if you need several different Random objects, the best way to do that is to call Random::combineSeed() on the result to permute it with a constant value.