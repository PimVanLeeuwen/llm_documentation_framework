#### drawAt()


 void Drawable::drawAt ( Graphics & g, 
 
 float x, 
 float y, 
 float opacity ) const 

Renders the Drawable at a given offset within the Graphics context.The coordinates passedin are used to translate the object relative to its own origin before drawing it this is basically a quick way of saying:draw (g, AffineTransform::translation (x, y)).
AffineTransform::translationstatic AffineTransform translation(float deltaX, float deltaY) noexceptReturns a new transform which is a translation.
Drawable::drawvoid draw(Graphics &g, float opacity, const AffineTransform &transform=AffineTransform()) constRenders this Drawable object.
xfloat xDefinition juce\_UnityPluginInterface.h:200
yfloat float yDefinition juce\_UnityPluginInterface.h:200
Note that the preferred way to render a drawable in future is by using it as a component and adding it to a parent, so you might want to consider that before using this method.