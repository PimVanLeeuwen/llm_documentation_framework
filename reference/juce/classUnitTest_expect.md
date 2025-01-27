#### expect()


 void UnitTest::expect ( bool testResult, 
 
 const String & failureMessage = String() ) 

Checks that the result of a test is true, and logs this result.In your runTest() method, you should call this method for each condition that you want to check, e.g.void runTest()
{
 beginTest ("basic tests");
 expect (x + y == 2);
 expect (getThing() == someThing);
 ...etc...
}
xfloat xDefinition juce\_UnityPluginInterface.h:200
yfloat float yDefinition juce\_UnityPluginInterface.h:200
If testResult is true, a pass is logged; if it's false, a failure is logged. If the failure message is specified, it will be written to the log if the test fails.