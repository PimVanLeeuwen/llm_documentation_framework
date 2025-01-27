#### setRepaintsOnMouseActivity()


 void Component::setRepaintsOnMouseActivity ( bool shouldRepaint ) noexcept 
 

Causes automatic repaints when the mouse enters or exits this component.If turned on, then when the mouse enters/exits, or when the button is pressed/released on the component, it will trigger a repaint.This is handy for things like buttons that need to draw themselves differently when the mouse moves over them, and it avoids having to override all the different mouse callbacks and call repaint().See alsomouseEnter, mouseExit, mouseDown, mouseUp