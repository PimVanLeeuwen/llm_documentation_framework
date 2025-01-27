#### valueToProportionOfLength()


 virtual double Slider::valueToProportionOfLength ( double value ) virtual 
 

Allows a userdefined mapping of value to the position of the slider along its length.The default implementation for this performs the skewing operation that can be set up in the setSkewFactor() method. Override it if you need some kind of custom mapping instead, but make sure you also implement the inverse function in proportionOfLengthToValue().Parameters

 value a valid slider value, between the range of values specified in setRange() 
 



Returnsa value 0 to 1.0 indicating the distance along the slider that represents this value 
See alsoproportionOfLengthToValue