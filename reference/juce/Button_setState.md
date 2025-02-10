#### setState()


 void Button::setState ( ButtonState newState ) 
 

Can be used to force the button into a particular state.This only changes the button's appearance, it won't trigger a click, or stop any mouseclicks from happening.The state that you set here will only last until it is automatically changed when the mouse enters or exits the button, or the mousebutton is pressed or released.