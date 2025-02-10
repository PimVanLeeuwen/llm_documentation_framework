#### applyEffect()


 void DropShadowEffect::applyEffect ( Image & sourceImage, Graphics & destContext, float scaleFactor, float alpha ) overridevirtual 
 

Overridden to render the effect.The implementation of this method must use the image that is passed in as its source, and should render its output to the graphics context passed in.Parameters

 sourceImage the image that the source component has just rendered with its paint() method. The image may or may not have an alpha channel, depending on whether the component is opaque. 
 
 destContext the graphics context to use to draw the resultant image. 
 scaleFactor a scale factor that has been applied to the image e.g. if this is 2, then the image is actually scaledup to twice the original resolution 
 alpha the alpha with which to draw the resultant image to the target context 


Implements ImageEffectFilter.