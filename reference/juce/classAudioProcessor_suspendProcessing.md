#### suspendProcessing()


 void AudioProcessor::suspendProcessing ( bool shouldBeSuspended ) 
 

Enables and disables the processing callback.If you need to do something timeconsuming on a thread and would like to make sure the audio processing callback doesn't happen until you've finished, use this to disable the callback and reenable it again afterwards.E.g.void loadNewPatch()
{
 suspendProcessing (true);
 
 ..do something that takes ages..
 
 suspendProcessing (false);
}
AudioProcessor::suspendProcessingvoid suspendProcessing(bool shouldBeSuspended)Enables and disables the processing callback.
If the host tries to make an audio callback while processing is suspended, the processor will return an empty buffer, but won't block the audio thread like it would do if you use the getCallbackLock() critical section to synchronise access.Any code that calls processBlock() should call isSuspended() before doing so, and if the processor is suspended, it should avoid the call and emit silence or whatever is appropriate.See alsogetCallbackLock