#### setDrawableTransform()


 void Drawable::setDrawableTransform ( const AffineTransform & transform ) 
 

Sets a transformation that applies to the same coordinate system in which the rest of the draw calls are made.You almost certainly want to call this function when working with Drawables as opposed to Component::setTransform().The reason for this is that the origin of a Drawable is not the same as the point returned by Component::getPosition() but has an additional offset internal to the Drawable class.Using setDrawableTransform() will take this internal offset into account when applying the transform to the Component base.You can only use Drawable::setDrawableTransform() or Component::setTransform() for a given object. Using both will lead to unpredictable behaviour.