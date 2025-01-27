#### withExtraKerningFactor()


 Font Font::withExtraKerningFactor ( float extraKerning ) const nodiscard 
 

Returns a copy of this font with a new tracking factor.Parameters

 extraKerning a multiple of the font's height that will be added to space between the characters. So a value of zero is normal spacing, positive values spread the letters out, negative values make them closer together.