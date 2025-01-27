#### notifyContentChanged()


 void ARAAudioSource::notifyContentChanged ( ARAContentUpdateScopes scopeFlags, 
 
 bool notifyARAHost ) 

Notify the ARA host and any listeners of a content update initiated by the plugin.This must be called by the plugin model management code on the message thread whenever updating the internal content representation, such as after successfully analyzing a new tempo map. Listeners will be notified immediately. If `notifyARAHost` is true, a notification to the host will be enqueued and sent out the next time it polls for updates. `notifyARAHost` must be false if the update was triggered by the host via doUpdateAudioSourceContent(). Furthermore, `notifyARAHost` must be false if the updated content is being restored from an archive.Parameters

 scopeFlags The scope of the content update. 
 
 notifyARAHost If true, the ARA host will be notified of the content change. 




Member Data Documentation