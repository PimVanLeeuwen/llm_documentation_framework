#### clip()


template<typename FloatType , typename CountType > 

 static void JUCE\_CALLTYPE FloatVectorOperationsBase< FloatType, CountType >::clip ( FloatType \* dest, const FloatType \* src, FloatType low, FloatType high, CountType num ) staticnoexcept 
 

Each element of dest is calculated by hard clipping the corresponding src element so that it is in the range specified by the arguments low and high.