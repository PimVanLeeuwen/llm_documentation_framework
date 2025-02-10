#### applyToImage()


 void ImageConvolutionKernel::applyToImage ( Image & destImage, 
 
 const Image & sourceImage, 
 const Rectangle< int > & destinationArea ) const 

Applies the kernel to an image.Parameters

 destImage the image that will receive the resultant convoluted pixels. 
 
 sourceImage the source image to read from this can be the same image as the destination, but if different, it must be exactly the same size and format. 
 destinationArea the region of the image to apply the filter to