#### withStyle()


 FontOptions FontOptions::withStyle ( String x ) const nodiscard 
 

Returns a copy of these options with a new typeface style.If the options include a nonnull Typeface::Ptr, this will be ignored. Otherwise, a suitable typeface will be located based on the typeface name and style strings.References jassertfalse, withMember(), and x.