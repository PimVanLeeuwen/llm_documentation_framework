#### applyGaussianBlurEffect()


 virtual void ImagePixelData::applyGaussianBlurEffect ( float radius, Image & result ) virtual 
 

Applies a native blur effect to this image, if available.This blur applies to all channels of the input image. It may be more expensive to calculate than a box blur, but should produce higherquality results.Implementations should attempt to reuse the storage provided in the result outparameter when possible.If native blurs are unsupported, or if creating a blur fails for any other reason, the result outparameter will be reset to an invalid image.