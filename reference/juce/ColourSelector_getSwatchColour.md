#### getSwatchColour()


 virtual Colour ColourSelector::getSwatchColour ( int index ) const virtual 
 

Called by the selector to find out the colour of one of the swatches.Your subclass should return the colour of the swatch with the given index.To enable swatches, you'll need to override getNumSwatches(), getSwatchColour(), and setSwatchColour(), to return the number of colours you want, and to set and retrieve their values.