#### getTotalNumOutputChannels()


 int AudioProcessor::getTotalNumOutputChannels ( ) const noexcept 
 

Returns the total number of output channels.This method will return the total number of output channels by accumulating the number of channels on each output bus. The number of channels of the buffer passed to your processBlock callback will be equivalent to either getTotalNumInputChannels or getTotalNumOutputChannels which ever is greater.Note that getTotalNumOutputChannels is equivalent to getMainBusNumOutputChannels if your processor does not have any sidechains or aux buses.