#### fillWindowingTables() [2/2]


template<typename FloatType > 

 static void dsp::WindowingFunction< FloatType >::fillWindowingTables ( FloatType \* samples, size\_t size, WindowingMethod , bool normalise = true, FloatType beta = 0 ) staticnoexcept 
 

Fills the content of an array with a given windowing method table.Parameters

 samples the destination buffer pointer 
 
 size the size of the destination buffer allocated in the object 
 normalise if the result must be normalised, creating a DC amplitude response of one 
 beta an optional argument useful only for Kaiser's method, which must be positive and sets the properties of the method (bandwidth and attenuation increases with beta)