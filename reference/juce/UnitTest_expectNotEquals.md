#### expectNotEquals()


template<class ValueType > 

 void UnitTest::expectNotEquals ( ValueType value, 
 
 ValueType valueToCompareTo, 
 String failureMessage = String() ) 

Checks whether a value is not equal to a comparison value.If this check fails, prints out a message containing the actual and comparison values.References exactlyEqual().