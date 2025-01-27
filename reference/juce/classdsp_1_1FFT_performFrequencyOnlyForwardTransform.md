#### performFrequencyOnlyForwardTransform()


 void dsp::FFT::performFrequencyOnlyForwardTransform ( float \* inputOutputData, bool onlyCalculateNonNegativeFrequencies = false ) const noexcept 
 

Takes an array and simply transforms it to the magnitude frequency response spectrum.This may be handy for things like frequency displays or analysis. The size of the array passed in must be 2 \* getSize().On return, if onlyCalculateNonNegativeFrequencies is false, the array will contain size magnitude values. If onlyCalculateNonNegativeFrequencies is true, the array will contain at least size / 2 + 1 magnitude values.