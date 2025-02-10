#### setKernelValue()


 void ImageConvolutionKernel::setKernelValue ( int x, int y, float value ) noexcept 
 

Sets the value of a specific cell in the kernel.The x and y parameters must be in the range 0 < x < getKernelSize().See alsosetOverallSum