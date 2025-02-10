#### performRealOnlyInverseTransform()


 void dsp::FFT::performRealOnlyInverseTransform ( float \* inputOutputData ) const noexcept 
 

Performs a reverse operation to data created in performRealOnlyForwardTransform().Although performRealOnlyInverseTransform will only use the first ((size / 2) + 1) complex numbers, the size of the array passed in must still be 2 \* getSize(), as some FFT engines require the extra space for the calculation. On return, the first half of the array will contain the reconstituted samples.