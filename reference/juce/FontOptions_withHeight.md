#### withHeight()


 FontOptions FontOptions::withHeight ( float x ) const nodiscard 
 

Returns a copy of these options with the specified height in JUCE units (can be fractional).FontOptions can hold either a JUCE height, set via withHeight(), or a point height, set via withPointHeight(). After calling withHeight(), the result of getPointHeight() will be 1.0f to indicate that the point height is unset.For more information about how JUCE font heights work, see Font::setHeight().References jassert, and x.