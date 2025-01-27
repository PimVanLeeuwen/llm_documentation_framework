#### multiplyAllAlphas()


 void Image::multiplyAllAlphas ( float amountToMultiplyBy ) 
 

Changes the overall opacity of the image.This will multiply the alpha value of each pixel in the image by the given amount (limiting the resulting alpha values between 0 and 255). This allows you to make an image more or less transparent.If the image doesn't have an alpha channel, this won't have any effect.