#### getPositionOfValue()


 float Slider::getPositionOfValue ( double value ) const 
 

Returns the X or Y coordinate of a value along the slider's length.If the slider is horizontal, this will be the X coordinate of the given value, relative to the left of the slider. If it's vertical, then this will be the Y coordinate, relative to the top of the slider.If the slider is rotary, this will throw an assertion and return 0. If the value is outofrange, it will be constrained to the length of the slider.