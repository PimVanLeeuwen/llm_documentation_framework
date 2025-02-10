#### mouseDown()


template<typename Type > 

 void Draggable3DOrientation::mouseDown ( Point< Type > mousePos ) noexcept 
 

Begins a mousedrag operation.You must call this before any calls to mouseDrag(). The position that is supplied will be treated as being relative to the centre of the rectangle passed to setViewport().