#### createComponentSnapshot()


 Image Component::createComponentSnapshot ( Rectangle< int > areaToGrab, 
 
 bool clipImageToComponentBounds = true, 
 float scaleFactor = 1.0f ) 

Generates a snapshot of part of this component.This will return a new Image, the size of the rectangle specified, containing a snapshot of the specified area of the component and all its children.The image may or may not have an alphachannel, depending on whether the image is opaque or not.If the clipImageToComponentBounds parameter is true and the area is greater than the size of the component, it'll be clipped. If clipImageToComponentBounds is false then parts of the component beyond its bounds can be drawn.See alsopaintEntireComponent