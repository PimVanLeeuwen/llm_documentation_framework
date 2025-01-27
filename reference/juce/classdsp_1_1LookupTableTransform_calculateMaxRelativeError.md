#### calculateMaxRelativeError()


template<typename FloatType > 

 static double dsp::LookupTableTransform< FloatType >::calculateMaxRelativeError ( const std::function< FloatType(FloatType)> & functionToApproximate, FloatType minInputValue, FloatType maxInputValue, size\_t numPoints, size\_t numTestPoints = 0 ) static 
 

Calculates the maximum relative error of the approximation for the specified parameter set.The closer the returned value is to zero the more accurate the approximation is.This function compares the approximated output of this class to the function it approximates at a range of points and returns the maximum relative error. This can be used to determine if the approximation is suitable for the given problem. The accuracy of the approximation can generally be improved by increasing numPoints.Parameters

 functionToApproximate The approximated function. This should be a mapping from a FloatType to FloatType. 
 
 minInputValue The lowest input value used. 
 maxInputValue The highest input value used. 
 numPoints The number of precalculated values stored. 
 numTestPoints The number of input values used for error calculation. Higher numbers can increase the accuracy of the error calculation. If it's zero then 100 \* numPoints will be used.