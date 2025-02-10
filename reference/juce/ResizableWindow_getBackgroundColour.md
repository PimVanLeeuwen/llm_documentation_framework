#### getBackgroundColour()


 Colour ResizableWindow::getBackgroundColour ( ) const noexcept 
 

Returns the colour currently being used for the window's background.As a convenience the window will fill itself with this colour, but you can override the paint() method if you need more customised behaviour.This method is the same as retrieving the colour for ResizableWindow::backgroundColourId.See alsosetBackgroundColour