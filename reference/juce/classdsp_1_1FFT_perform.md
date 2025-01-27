#### perform()


 void dsp::FFT::perform ( const Complex< float > \* input, Complex< float > \* output, bool inverse ) const noexcept 
 

Performs an outofplace FFT, either forward or inverse.The arrays must contain at least getSize() elements.