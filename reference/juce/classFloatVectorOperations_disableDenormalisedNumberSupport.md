#### disableDenormalisedNumberSupport()


 static void JUCE\_CALLTYPE FloatVectorOperations::disableDenormalisedNumberSupport ( bool shouldDisable = true ) staticnoexcept 
 

On Intel CPUs, this method enables the SSE flushtozero and denormalisedarezero modes.This effectively sets the DAZ and FZ bits of the MXCSR register. On arm CPUs this will enable flush to zero mode. It's a convenient thing to call before audio processing code where you really want to avoid denormalisation performance hits.