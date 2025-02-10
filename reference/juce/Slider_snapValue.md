#### snapValue()


 virtual double Slider::snapValue ( double attemptedValue, DragMode dragMode ) virtual 
 

This can be overridden to allow the slider to snap to userdefinable values.If overridden, it will be called when the user tries to move the slider to a given position, and allows a subclass to sanitycheck this value, possibly returning a different value to use instead.Parameters

 attemptedValue the value the user is trying to enter 
 
 dragMode indicates whether the user is dragging with the mouse; notDragging if they are entering the value using the text box or other nondragging interaction 



Returnsthe value to use instead