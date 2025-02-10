#### setScrollOnDragMode()


 void Viewport::setScrollOnDragMode ( ScrollOnDragMode scrollOnDragMode ) 
 

Sets the current scrollondrag mode.The default is ScrollOnDragMode::nonHover.If your viewport contains a Component that you don't want to receive mouse events when the user is dragscrolling, you can disable this with the Component::setViewportIgnoreDragFlag() method.