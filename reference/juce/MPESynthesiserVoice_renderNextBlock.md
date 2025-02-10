#### renderNextBlock() [2/2]


 virtual void MPESynthesiserVoice::renderNextBlock ( AudioBuffer< double > & , int , int ) virtual 
 

Renders the next block of 64bit data for this voice.Support for 64bit audio is optional. You can choose to not override this method if you don't need it (the default implementation simply does nothing).