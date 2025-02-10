#### setImages()


 void ImageButton::setImages ( bool resizeButtonNowToFitThisImage, 
 
 bool rescaleImagesWhenButtonSizeChanges, 
 bool preserveImageProportions, 
 const Image & normalImage, 
 float imageOpacityWhenNormal, 
 Colour overlayColourWhenNormal, 
 const Image & overImage, 
 float imageOpacityWhenOver, 
 Colour overlayColourWhenOver, 
 const Image & downImage, 
 float imageOpacityWhenDown, 
 Colour overlayColourWhenDown, 
 float hitTestAlphaThreshold = 0.0f ) 

Sets up the images to draw in various states.Parameters

 resizeButtonNowToFitThisImage if true, the button will be immediately resized to the same dimensions as the normal image 
 
 rescaleImagesWhenButtonSizeChanges if true, the image will be rescaled to fit the button when the button's size changes 
 preserveImageProportions if true then any rescaling of the image to fit the button will keep the image's x and y proportions correct i.e. it won't distort its shape, although this might create gaps around the edges 
 normalImage the image to use when the button is in its normal state. button no longer needs it. 
 imageOpacityWhenNormal the opacity to use when drawing the normal image. 
 overlayColourWhenNormal an overlay colour to use to fill the alpha channel of the normal image if this colour is transparent, no overlay will be drawn. The overlay will be drawn over the top of the image, so you can basically add a solid or semitransparent colour to the image to brighten or darken it 
 overImage the image to use when the mouse is over the button. If you want to use the same image as was set in the normalImage parameter, this value can be a null image. 
 imageOpacityWhenOver the opacity to use when drawing the image when the mouse is over the button 
 overlayColourWhenOver an overlay colour to use to fill the alpha channel of the image when the mouse is over if this colour is transparent, no overlay will be drawn 
 downImage an image to use when the button is pressed down. If set to a null image, the 'over' image will be drawn instead (or the normal image if there isn't an 'over' image either). 
 imageOpacityWhenDown the opacity to use when drawing the image when the button is pressed 
 overlayColourWhenDown an overlay colour to use to fill the alpha channel of the image when the button is pressed down if this colour is transparent, no overlay will be drawn 
 hitTestAlphaThreshold if set to zero, the mouse is considered to be over the button whenever it's inside the button's bounding rectangle. If set to values higher than 0, the mouse will only be considered to be over the image when the value of the image's alpha channel at that position is greater than this level.