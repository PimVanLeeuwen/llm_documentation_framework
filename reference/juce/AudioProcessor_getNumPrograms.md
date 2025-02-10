#### getNumPrograms()


 virtual int AudioProcessor::getNumPrograms ( ) pure virtual 
 

Returns the number of preset programs the processor supports.The value returned must be valid as soon as this object is created, and must not change over its lifetime.This value shouldn't be less than 1.Implemented in AudioProcessorGraph::AudioGraphIOProcessor, and AudioProcessorGraph.