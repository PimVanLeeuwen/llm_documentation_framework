#### toString()


template<typename Type > 

 static String Decibels::toString ( Type decibels, int decimalPlaces = 2, Type minusInfinityDb = Type (defaultMinusInfinitydB), bool shouldIncludeSuffix = true, StringRef customMinusInfinityString = {} ) static 
 

Converts a decibel reading to a string.By default the returned string will have the 'dB' suffix added, but this can be removed by setting the shouldIncludeSuffix argument to false. If a customMinusInfinityString argument is provided this will be returned if the value is lower than minusInfinityDb, otherwise the return value will be "INF".