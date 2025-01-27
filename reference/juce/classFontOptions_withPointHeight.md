#### withPointHeight()


 FontOptions FontOptions::withPointHeight ( float x ) const nodiscard 
 

Returns a copy of these options with the specified height in points (can be fractional).After calling withPointHeight(), the result of getHeight() will be 1.0f to indicate that the JUCE height is unset.For more information about how point heights work, see Font::setPointHeight().References jassert, and x.