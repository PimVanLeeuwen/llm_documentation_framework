#### setColour()


 void Component::setColour ( int colourID, 
 
 Colour newColour ) 

Registers a colour to be used for a particular purpose.Changing a colour will cause a synchronous callback to the colourChanged() method, which your component can override if it needs to do something when colours are altered.Note repaint() is not automatically called when a colour is changed.For more details about colour IDs, see the comments for findColour().See alsofindColour, isColourSpecified, colourChanged, LookAndFeel::findColour, LookAndFeel::setColour