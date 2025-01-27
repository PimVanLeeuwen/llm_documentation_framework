#### addDummyOversamplingStage()


template<typename SampleType > 

 void dsp::Oversampling< SampleType >::addDummyOversamplingStage ( ) 
 

Adds a new "dummy" oversampling stage, which does nothing to the signal.Using one can be useful if your application features a customisable oversampling factor and if you want to select the current one from an OwnedArray without changing anything in the processing code.See alsoOwnedArray, clearOversamplingStages, addOversamplingStage