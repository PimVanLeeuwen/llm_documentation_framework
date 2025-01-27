#### exp() [2/2]


template<typename FloatType > 

 static void dsp::FastMathApproximations::exp ( FloatType \* values, size\_t numValues ) staticnoexcept 
 

Provides a fast approximation of the function exp(x) using a Pade approximant continued fraction, calculated on a whole buffer.Note: This is an approximation which works on a limited range. You are advised to use input values only between 6 and +4 for limiting the error.References exp().