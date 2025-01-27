#### runTestsInCategory()


 void UnitTestRunner::runTestsInCategory ( const String & category, 
 
 int64 randomSeed = 0 ) 

Runs all the UnitTest objects within a specified category.This calls runTests() for all the objects listed in UnitTest::getTestsInCategory().If you want to run the tests with a predetermined seed, you can pass that into the randomSeed argument, or pass 0 to have a randomlygenerated seed chosen.