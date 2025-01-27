#### getChannelCountOfBus()


 int AudioProcessor::getChannelCountOfBus ( bool isInput, int busIndex ) const noexcept 
 

Provides the number of channels of the bus with a given index and direction.If the index, direction combination is invalid then this will return zero.