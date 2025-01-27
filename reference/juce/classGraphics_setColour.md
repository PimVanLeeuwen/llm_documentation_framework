#### setColour()


 void Graphics::setColour ( Colour newColour ) 
 

Changes the current drawing colour.This sets the colour that will now be used for drawing operations it also sets the opacity to that of the colour passedin.If a brush is being used when this method is called, the brush will be deselected, and any subsequent drawing will be done with a solid colour brush instead.See alsosetOpacity