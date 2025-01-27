#### setOpacity()


 void Graphics::setOpacity ( float newOpacity ) 
 

Changes the opacity to use with the current colour.If a solid colour is being used for drawing, this changes its opacity to this new value (i.e. it doesn't multiply the colour's opacity by this amount).If a gradient is being used, this will have no effect on it.A value of 0.0 is completely transparent, 1.0 is completely opaque.