#### addTransform()


 void Graphics::addTransform ( const AffineTransform & transform ) 
 

Adds a transformation which will be performed on all the graphics operations that the context subsequently performs.After calling this, all the coordinates that are passed into the context will be transformed by this matrix.See alsosetOrigin