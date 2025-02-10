#### runTests()


 void UnitTestRunner::runTests ( const Array< UnitTest \* > & tests, 
 
 int64 randomSeed = 0 ) 

Runs a set of tests.The tests are performed in order, and the results are logged. To run all the registered UnitTest objects that exist, use runAllTests().If you want to run the tests with a predetermined seed, you can pass that into the randomSeed argument, or pass 0 to have a randomlygenerated seed chosen.