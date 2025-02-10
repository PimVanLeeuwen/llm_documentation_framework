#### setSkewFactor()


 void Slider::setSkewFactor ( double factor, 
 
 bool symmetricSkew = false ) 

Sets up a skew factor to alter the way values are distributed.You may want to use a range of values on the slider where more accuracy is required towards one end of the range, so this will logarithmically spread the values across the length of the slider.If the factor is < 1.0, the lower end of the range will fill more of the slider's length; if the factor is > 1.0, the upper end of the range will be expanded instead. A factor of 1.0 doesn't skew it at all.If symmetricSkew is true, the skew factor applies from the middle of the slider to each of its ends.To set the skew position by using a midpoint, use the setSkewFactorFromMidPoint() method instead.See alsogetSkewFactor, setSkewFactorFromMidPoint, isSymmetricSkew