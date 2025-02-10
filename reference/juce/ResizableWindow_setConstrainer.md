#### setConstrainer()


 void ResizableWindow::setConstrainer ( ComponentBoundsConstrainer \* newConstrainer ) 
 

Sets the boundsconstrainer object to use for resizing and dragging this window.A pointer to the object you pass in will be kept, but it won't be deleted by this object, so it's the caller's responsibility to manage it.If you pass a nullptr, then no constraints will be placed on the positioning of the window.Referenced by StandaloneFilterWindow::StandaloneFilterWindow().