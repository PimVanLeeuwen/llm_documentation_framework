#### withRotatedHue()


 Colour Colour::withRotatedHue ( float amountToRotate ) const nodiscardnoexcept 
 

Returns a copy of this colour with its hue rotated.The new colour's hue is ((this>getHue() + amountToRotate) % 1.0)See alsobrighter, darker, withMultipliedBrightness