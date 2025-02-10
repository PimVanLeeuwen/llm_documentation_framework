#### setViewport()


 void Draggable3DOrientation::setViewport ( Rectangle< int > newArea ) noexcept 
 

Sets the viewport area within which mousedrag positions will occur.You'll need to set this rectangle before calling mouseDown. The centre of the rectangle is assumed to be the centre of the object that will be rotated, and the size of the rectangle will be used to scale the object radius see setRadius().