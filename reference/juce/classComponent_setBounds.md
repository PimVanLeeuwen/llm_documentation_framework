#### setBounds() [2/2]


 void Component::setBounds ( Rectangle< int > newBounds ) 
 

Changes the component's position and size.The coordinates are relative to the topleft of the component's parent, or relative to the origin of the screen if the component is on the desktop.If this method changes the component's topleft position, it will make a synchronous call to moved(). If it changes the size, it will also make a call to resized().Note that if you've used setTransform() to apply a transform, then the component's bounds will no longer be a direct reflection of the position at which it appears within its parent, as the transform will be applied to whatever bounds you set for it.See alsosetBounds