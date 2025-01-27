#### draw() [2/2]


 void GlyphArrangement::draw ( const Graphics & , 
 
 AffineTransform ) const 

Draws this glyph arrangement to a graphics context.This renders the paths as filled vectors, so is far slower than the draw (Graphics&) method for nontransformed arrangements.