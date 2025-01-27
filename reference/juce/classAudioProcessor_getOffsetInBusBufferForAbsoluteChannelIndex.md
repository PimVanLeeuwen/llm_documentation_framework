#### getOffsetInBusBufferForAbsoluteChannelIndex()


 int AudioProcessor::getOffsetInBusBufferForAbsoluteChannelIndex ( bool isInput, int absoluteChannelIndex, int & busIndex ) const noexcept 
 

Returns the offset in a bus's buffer from an absolute channel index.This method returns the offset in a bus's buffer given an absolute channel index. It also provides the bus index. For example, this method would return one for a processor with two stereo buses when given the absolute channel index.