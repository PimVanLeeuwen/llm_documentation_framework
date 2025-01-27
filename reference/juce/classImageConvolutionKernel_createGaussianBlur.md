#### createGaussianBlur()


 void ImageConvolutionKernel::createGaussianBlur ( float blurRadius ) 
 

Initialises the kernel for a gaussian blur.Parameters

 blurRadius this may be larger or smaller than the kernel's actual size but this will obviously be wasteful or clip at the edges. Ideally the kernel should be just larger than (blurRadius \* 2).