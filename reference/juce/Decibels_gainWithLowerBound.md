#### gainWithLowerBound()


template<typename Type > 

 static Type Decibels::gainWithLowerBound ( Type gain, Type lowerBoundDb ) static 
 

Restricts a gain value based on a lower bound specified in dBFS.This is useful if you want to make sure a gain value never reaches zero.References decibelsToGain(), jassert, and jmax().