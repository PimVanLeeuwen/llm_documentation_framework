#### setTriggeredOnMouseDown()


 void Button::setTriggeredOnMouseDown ( bool isTriggeredOnMouseDown ) noexcept 
 

Sets whether the button click should happen when the mouse is pressed or released.By default the button is only considered to have been clicked when the mouse is released, but setting this to true will make it call the clicked() method as soon as the button is pressed.This is useful if the button is being used to show a popup menu, as it allows the click to be used as a drag onto the menu.Referenced by StandaloneFilterWindow::StandaloneFilterWindow().