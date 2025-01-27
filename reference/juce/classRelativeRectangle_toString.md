#### toString()


 String RelativeRectangle::toString ( ) const 
 

Returns a string which represents this point.This returns a commaseparated list of coordinates, in the order left, top, right, bottom. If you're using this to position a Component, then see the notes for Component::setBounds (const RelativeRectangle&) for details of the syntax used. The string that is returned can be passed to the RelativeRectangle constructor to recreate the rectangle.