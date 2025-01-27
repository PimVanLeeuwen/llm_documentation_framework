#### createLookupTable() [3/3]


template<size\_t NumEntries> 

 void ColourGradient::createLookupTable ( PixelARGB(&) resultLookupTable[NumEntries] ) const noexcept 
 

Creates a set of interpolated premultiplied ARGB values.This will fill an array of a userspecified size with the gradient, interpolating to fit. When calling this, the ColourGradient must have at least 2 colour stops specified.