#### runAllTests()


 void UnitTestRunner::runAllTests ( int64 randomSeed = 0 ) 
 

Runs all the UnitTest objects that currently exist.This calls runTests() for all the objects listed in UnitTest::getAllTests().If you want to run the tests with a predetermined seed, you can pass that into the randomSeed argument, or pass 0 to have a randomlygenerated seed chosen.