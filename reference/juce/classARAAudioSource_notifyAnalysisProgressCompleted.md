#### notifyAnalysisProgressCompleted()


 void ARAAudioSource::notifyAnalysisProgressCompleted ( ) 
 

Notify the ARA host and any listeners of analysis progress.Contrary to most ARA functions, this call can be made from any thread. The implementation will enqueue these notifications and later post them from the message thread. Calling code must ensure start and completion state are always balanced, and must send updates in ascending order.