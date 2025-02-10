#### setResizable()


 void ResizableWindow::setResizable ( bool shouldBeResizable, 
 
 bool useBottomRightCornerResizer ) 

Make the window resizable or fixed.Parameters

 shouldBeResizable whether it's resizable at all 
 
 useBottomRightCornerResizer if true, it'll add a ResizableCornerComponent at the bottomright; if false, it'll use a ResizableBorderComponent around the edge 



See alsosetResizeLimits, isResizable Referenced by StandaloneFilterWindow::StandaloneFilterWindow().