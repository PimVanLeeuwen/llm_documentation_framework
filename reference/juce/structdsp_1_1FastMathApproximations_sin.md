#### sin() [2/2]


template<typename FloatType > 

 static void dsp::FastMathApproximations::sin ( FloatType \* values, size\_t numValues ) staticnoexcept 
 

Provides a fast approximation of the function sin(x) using a Pade approximant continued fraction, calculated on a whole buffer.Note: This is an approximation which works on a limited range. You are advised to use input values only between pi and +pi for limiting the error.References sin().