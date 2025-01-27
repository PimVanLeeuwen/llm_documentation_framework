#### setViewPosition() [2/2]


 void Viewport::setViewPosition ( Point< int > newPosition ) 
 

Changes the position of the viewed component.The inner component will be moved so that the pixel at the top left of the viewport will be the pixel at the specified coordinates within the inner component.This will update the scrollbars and might cause a call to visibleAreaChanged().See alsogetViewPositionX, getViewPositionY, setViewPositionProportionately