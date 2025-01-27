#### setTextValueSuffix()


 void Slider::setTextValueSuffix ( const String & suffix ) 
 

Sets a suffix to append to the end of the numeric value when it's displayed as a string.This is used by the default implementation of getTextFromValue(), and is just appended to the numeric value. For more advanced formatting, you can override getTextFromValue() and do something else.