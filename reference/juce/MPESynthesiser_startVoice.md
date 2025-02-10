#### startVoice()


 void MPESynthesiser::startVoice ( MPESynthesiserVoice \* voice, MPENote noteToStart ) protected 
 

Starts a specified voice and tells it to play a particular MPENote.You should never need to call this, it's called internally by MPESynthesiserBase::instrument via the noteStarted callback, but is protected in case it's useful for some custom subclasses.