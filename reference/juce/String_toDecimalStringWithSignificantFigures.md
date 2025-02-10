#### toDecimalStringWithSignificantFigures()


template<typename DecimalType > 

 static String String::toDecimalStringWithSignificantFigures ( DecimalType number, int numberOfSignificantFigures ) static 
 

Returns a string containing a decimal with a set number of significant figures.Parameters

 number the input number 
 
 numberOfSignificantFigures the number of significant figures to use 


References exactlyEqual(), jassert, and shift.