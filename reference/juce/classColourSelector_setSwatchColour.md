#### setSwatchColour()


 virtual void ColourSelector::setSwatchColour ( int index, const Colour & newColour ) virtual 
 

Called by the selector when the user puts a new colour into one of the swatches.Your subclass should change the colour of the swatch with the given index.To enable swatches, you'll need to override getNumSwatches(), getSwatchColour(), and setSwatchColour(), to return the number of colours you want, and to set and retrieve their values.