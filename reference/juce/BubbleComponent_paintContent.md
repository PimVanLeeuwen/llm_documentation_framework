#### paintContent()


 virtual void BubbleComponent::paintContent ( Graphics & g, int width, int height ) protectedpure virtual 
 

Subclasses should override this to draw their bubble's contents.The graphics object's clip region and the dimensions passed in here are set up to paint just the rectangle inside the bubble.Implemented in BubbleMessageComponent.