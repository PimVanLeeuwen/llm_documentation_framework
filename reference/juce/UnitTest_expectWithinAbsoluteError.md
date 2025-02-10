#### expectWithinAbsoluteError()


template<class ValueType > 

 void UnitTest::expectWithinAbsoluteError ( ValueType actual, 
 
 ValueType expected, 
 ValueType maxAbsoluteError, 
 String failureMessage = String() ) 

Computes the difference between a value and a comparison value, and if it is larger than a specified maximum value, prints out a message containing the actual and comparison values and the maximum allowed error.