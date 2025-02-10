#### drawWithin()


 void Drawable::drawWithin ( Graphics & g, 
 
 Rectangle< float > destArea, 
 RectanglePlacement placement, 
 float opacity ) const 

Renders the Drawable within a rectangle, scaling it to fit neatly inside without changing its aspectratio.The object can placed arbitrarily within the rectangle based on a Justification type, and can either be made as big as possible, or just reduced to fit.Note that the preferred way to render a drawable in future is by using it as a component and adding it to a parent, so you might want to consider that before using this method.Parameters

 g the graphics context to render onto 
 
 destArea the target rectangle to fit the drawable into 
 placement defines the alignment and rescaling to use to fit this object within the target rectangle. 
 opacity the opacity to use, in the range 0 to 1.0