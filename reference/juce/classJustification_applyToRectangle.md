#### applyToRectangle()


template<typename ValueType > 

 void Justification::applyToRectangle ( ValueType & x, ValueType & y, ValueType w, ValueType h, ValueType spaceX, ValueType spaceY, ValueType spaceW, ValueType spaceH ) const noexcept 
 

Adjusts the position of a rectangle to fit it into a space.The (x, y) position of the rectangle will be updated to position it inside the given space according to the justification flags.References bottom, h, horizontallyCentred, right, verticallyCentred, w, x, and y.Referenced by appliedToRectangle().