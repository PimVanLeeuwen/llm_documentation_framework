#### proportionOfLengthToValue()


 virtual double Slider::proportionOfLengthToValue ( double proportion ) virtual 
 

Allows a userdefined mapping of distance along the slider to its value.The default implementation for this performs the skewing operation that can be set up in the setSkewFactor() method. Override it if you need some kind of custom mapping instead, but make sure you also implement the inverse function in valueToProportionOfLength().Parameters

 proportion a value 0 to 1.0, indicating a distance along the slider 
 



Returnsthe slider value that is represented by this position 
See alsovalueToProportionOfLength