#### setPopupDisplayEnabled()


 void Slider::setPopupDisplayEnabled ( bool shouldShowOnMouseDrag, 
 
 bool shouldShowOnMouseHover, 
 Component \* parentComponentToUse, 
 int hoverTimeout = 2000 ) 

If enabled, this gives the slider a popup bubble which appears while the slider is being dragged or hoveredover.This can be handy if your slider doesn't have a textbox, so that users can see the value just when they're changing it.If you pass a component as the parentComponentToUse parameter, the popup bubble will be added as a child of that component when it's needed. If you pass nullptr, the popup will be placed on the desktop instead (note that it's a transparent window, so if you're using an OS that can't do transparent windows you'll have to add it to a parent component instead).By default the popup display shown when hovering will remain visible for 2 seconds, but it is possible to change this by passing a different hoverTimeout value. A value of 1 will cause the popup to remain until a mouseExit() occurs on the slider.