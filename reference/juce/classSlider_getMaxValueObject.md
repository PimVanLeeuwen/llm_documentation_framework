#### getMaxValueObject()


 Value & Slider::getMaxValueObject ( ) noexcept 
 

For a slider with two or three thumbs, this returns the higher of its values.You can use this Value object to connect the slider's position to external values or setters, either by taking a copy of the Value, or by using Value::referTo() to make it point to your own Value object.See alsoValue, getMaxValue, getMinValueObject