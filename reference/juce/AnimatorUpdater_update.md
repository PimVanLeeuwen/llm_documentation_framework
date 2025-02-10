#### update() [2/2]


 void AnimatorUpdater::update ( double timestampMs ) 
 

Calls Animator::update() for all registered Animators that are still alive.References to deleted Animators are removed.The supplied timestamp should be monotonically increasing for correct behaviour. Ideally this should be a timestamp supplied by a VBlankAttachment. Consider using the VBlankAnimatorUpdater class, which takes care of supplying the right timestamp.See alsoVBlankAnimatorUpdater