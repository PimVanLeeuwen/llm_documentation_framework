#### initialise()


template<typename FloatType > 

 void dsp::LookupTable< FloatType >::initialise ( const std::function< FloatType(size\_t)> & functionToApproximate, 
 
 size\_t numPointsToUse ) 

Initialises or changes the parameters of a LookupTable object.This function can be used to change what function is approximated by an already constructed LookupTable along with the number of data points used. If the function to be approximated won't ever change, prefer using the nondefault constructor.Parameters

 functionToApproximate The function to be approximated. This should be a mapping from the integer range [0, numPointsToUse 1]. 
 
 numPointsToUse The number of precalculated values stored.