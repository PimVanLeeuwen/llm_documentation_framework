#### clear()


 void Image::clear ( const Rectangle< int > & area, 
 
 Colour colourToClearTo = Colour(0x00000000) ) 

Clears a section of the image with a given colour.This won't do any alphablending it just sets all pixels in the image to the given colour (which may be nonopaque if the image has an alpha channel).