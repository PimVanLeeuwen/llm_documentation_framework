#### tan() [2/2]


template<typename FloatType > 

 static void dsp::FastMathApproximations::tan ( FloatType \* values, size\_t numValues ) staticnoexcept 
 

Provides a fast approximation of the function tan(x) using a Pade approximant continued fraction, calculated on a whole buffer.Note: This is an approximation which works on a limited range. You are advised to use input values only between pi/2 and +pi/2 for limiting the error.References tan().