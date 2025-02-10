#### setOverlayColour()


 void DrawableImage::setOverlayColour ( Colour newOverlayColour ) 
 

Sets a colour to draw over the image's alpha channel.By default this is transparent so isn't drawn, but if you set a nontransparent colour here, then it will be overlaid on the image, using the image's alpha channel as a mask.This is handy for doing things like darkening or lightening an image by overlaying it with semitransparent black or white.