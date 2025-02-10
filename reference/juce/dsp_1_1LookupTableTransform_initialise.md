#### initialise()


template<typename FloatType > 

 void dsp::LookupTableTransform< FloatType >::initialise ( const std::function< FloatType(FloatType)> & functionToApproximate, 
 
 FloatType minInputValueToUse, 
 FloatType maxInputValueToUse, 
 size\_t numPoints ) 

Initialises or changes the parameters of a LookupTableTransform object.Parameters

 functionToApproximate The function to be approximated. This should be a mapping from a FloatType to FloatType. 
 
 minInputValueToUse The lowest input value used. The approximation will fail for values lower than this. 
 maxInputValueToUse The highest input value used. The approximation will fail for values higher than this. 
 numPoints The number of precalculated values stored. 


Referenced by dsp::LookupTableTransform< FloatType >::LookupTableTransform().