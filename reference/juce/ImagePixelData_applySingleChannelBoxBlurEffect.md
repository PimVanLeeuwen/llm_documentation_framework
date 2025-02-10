#### applySingleChannelBoxBlurEffect()


 virtual void ImagePixelData::applySingleChannelBoxBlurEffect ( int radius, Image & result ) virtual 
 

Applies a native blur effect to this image, if available.This is intended for blurring singlechannel images, which is useful when rendering drop shadows. This is implemented as several boxblurs in series. The results should be visually similar to a Gaussian blur, but less accurate.Implementations should attempt to reuse the storage provided in the result outparameter when possible.If native blurs are unsupported, or if creating a blur fails for any other reason, the result outparameter will be reset to an invalid image.