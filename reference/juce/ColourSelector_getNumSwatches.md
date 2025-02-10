#### getNumSwatches()


 virtual int ColourSelector::getNumSwatches ( ) const virtual 
 

Tells the selector how many preset colour swatches you want to have on the component.To enable swatches, you'll need to override getNumSwatches(), getSwatchColour(), and setSwatchColour(), to return the number of colours you want, and to set and retrieve their values.