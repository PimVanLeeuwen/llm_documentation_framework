#### setOverallSum()


 void ImageConvolutionKernel::setOverallSum ( float desiredTotalSum ) 
 

Rescales all values in the kernel to make the total add up to a fixed value.This will multiply all values in the kernel by (desiredTotalSum / currentTotalSum).