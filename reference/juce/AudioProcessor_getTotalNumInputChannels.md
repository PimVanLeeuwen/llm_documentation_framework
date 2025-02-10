#### getTotalNumInputChannels()


 int AudioProcessor::getTotalNumInputChannels ( ) const noexcept 
 

Returns the total number of input channels.This method will return the total number of input channels by accumulating the number of channels on each input bus. The number of channels of the buffer passed to your processBlock callback will be equivalent to either getTotalNumInputChannels or getTotalNumOutputChannels which ever is greater.Note that getTotalNumInputChannels is equivalent to getMainBusNumInputChannels if your processor does not have any sidechains or aux buses.