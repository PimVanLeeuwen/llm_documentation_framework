#### withMultipliedSaturationHSL()


 Colour Colour::withMultipliedSaturationHSL ( float multiplier ) const nodiscardnoexcept 
 

Returns a copy of this colour with its saturation multiplied by the given value.The new colour's saturation is (this>getSaturation() \* multiplier) (the result is clipped to legal limits).This will be in the HSL colour space.