#### getChannelIndexInProcessBlockBuffer()


 int AudioProcessor::getChannelIndexInProcessBlockBuffer ( bool isInput, int busIndex, int channelIndex ) const noexcept 
 

Returns the position of a bus's channels within the processBlock buffer.This can be called in processBlock to figure out which channel of the master AudioBuffer maps onto a specific bus's channel.