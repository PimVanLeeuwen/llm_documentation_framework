#### getExtraKerningFactor()


 float Font::getExtraKerningFactor ( ) const noexcept 
 

Returns the font's tracking, i.e.spacing applied between characters in addition to the kerning defined by the font.This is the extra space added between adjacent characters, as a proportion of the font's height.A value of zero is normal spacing, positive values will spread the letters out more, and negative values make them closer together.