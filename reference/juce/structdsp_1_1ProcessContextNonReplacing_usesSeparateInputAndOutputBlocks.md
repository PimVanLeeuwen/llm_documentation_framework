#### usesSeparateInputAndOutputBlocks()


template<typename ContextSampleType > 

 static constexpr bool dsp::ProcessContextNonReplacing< ContextSampleType >::usesSeparateInputAndOutputBlocks ( ) staticconstexpr 
 

All process context classes will define this constant method so that templated code can determine whether the input and output blocks refer to the same buffer, or to two different ones.

Member Data Documentation