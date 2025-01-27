#### applyGaussianBlurEffect()


 static void ImageEffects::applyGaussianBlurEffect ( float radius, const Image & input, Image & result ) static 
 

Applies a blur to this image, placing the blurred image in the result outparameter.This will attempt to call the applyGaussianBlurEffect() member of the input image's underlying ImagePixelData, which will use hardware acceleration if available. If this fails, then a software blur will be applied instead.This blur applies to all channels of the input image. It may be more expensive to calculate than a box blur, but should produce higherquality results.If result is already the correct size, then its storage will be reused directly. Otherwise, new storage may be allocated for the blurred image.