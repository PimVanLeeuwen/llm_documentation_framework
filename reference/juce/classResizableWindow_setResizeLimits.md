#### setResizeLimits()


 void ResizableWindow::setResizeLimits ( int newMinimumWidth, int newMinimumHeight, int newMaximumWidth, int newMaximumHeight ) noexcept 
 

This sets the maximum and minimum sizes for the window.If the window's current size is outside these limits, it will be resized to make sure it's within them.A direct call to setBounds() will bypass any constraint checks, but when the window is dragged by the user or resized by other indirect means, the constrainer will limit the numbers involved.See alsosetResizable, setFixedAspectRatio