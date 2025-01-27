#### moveToAbsolute()


 void RelativeRectangle::moveToAbsolute ( const Rectangle< float > & newPos, 
 
 const Expression::Scope \* scope ) 

Changes the values of this rectangle's coordinates to make it resolve to the specified position.Calling this will leave any anchor points unchanged, but will set any absolute or relative positions to whatever values are necessary to make the resultant position match the position that is provided.