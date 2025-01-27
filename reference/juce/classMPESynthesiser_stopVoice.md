#### stopVoice()


 void MPESynthesiser::stopVoice ( MPESynthesiserVoice \* voice, MPENote noteToStop, bool allowTailOff ) protected 
 

Stops a given voice and tells it to stop playing a particular MPENote (which should be the same note it is actually playing).You should never need to call this, it's called internally by MPESynthesiserBase::instrument via the noteReleased callback, but is protected in case it's useful for some custom subclasses.

Member Data Documentation