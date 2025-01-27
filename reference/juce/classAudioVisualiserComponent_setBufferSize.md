#### setBufferSize()


 void AudioVisualiserComponent::setBufferSize ( int bufferSize ) 
 

Changes the number of samples that the visualiser keeps in its history.Note that this value refers to the number of averaged sample blocks, and each block is calculated as the peak of a number of incoming audio samples. To set the number of incoming samples per block, use setSamplesPerBlock().