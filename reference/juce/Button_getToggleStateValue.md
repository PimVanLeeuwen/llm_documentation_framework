#### getToggleStateValue()


 Value & Button::getToggleStateValue ( ) noexcept 
 

Returns the Value object that represents the button's toggle state.You can use this Value object to connect the button's state to external values or setters, either by taking a copy of the Value, or by using Value::referTo() to make it point to your own Value object.See alsogetToggleState, Value