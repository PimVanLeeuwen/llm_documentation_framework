#### setTransform()


 void Component::setTransform ( const AffineTransform & transform ) 
 

Sets a transform matrix to be applied to this component.If you set a transform for a component, the component's position will be warped by it, relative to the component's parent's topleft origin. This means that the values you pass into setBounds() will no longer reflect the actual area within the parent that the component covers, as the bounds will be transformed and the component will probably end up actually appearing somewhere else within its parent.When using transforms you need to be extremely careful when converting coordinates between the coordinate spaces of different components or the screen you should always use getLocalPoint(), getLocalArea(), etc to do this, and never just manually add a component's position to a point in order to convert it between different components (but I'm sure you would never have done that anyway...).Currently, transforms are not supported for desktop windows, so the transform will be ignored if you put a component on the desktop.To remove a component's transform, simply pass AffineTransform() as the parameter to this method.