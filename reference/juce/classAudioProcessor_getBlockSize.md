#### getBlockSize()


 int AudioProcessor::getBlockSize ( ) const noexcept 
 

Returns the current typical block size that is being used.This can be called from your processBlock() method it's not guaranteed to be valid at any other time.Remember it's not the ONLY block size that may be used when calling processBlock, it's just the normal one. The actual block sizes used may be larger or smaller than this, and will vary between successive calls.