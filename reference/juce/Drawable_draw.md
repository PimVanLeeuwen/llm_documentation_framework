#### draw()


 void Drawable::draw ( Graphics & g, 
 
 float opacity, 
 const AffineTransform & transform = AffineTransform() ) const 

Renders this Drawable object.Note that the preferred way to render a drawable in future is by using it as a component and adding it to a parent, so you might want to consider that before using this method.See alsodrawWithin