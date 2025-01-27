#### update()


 Status Animator::update ( double timestampMs ) const 
 

Called periodically for active Animators by the AnimatorUpdater classes.The passed in timestamp must be monotonically increasing. This allows the underlying Animator to follow its progression towards completion.While you can call this function in special circumstances, you will generally want an AnimatorUpdater to do it. Using the VBlankAnimatorUpdater ensures that update is called in sync with the monitor's vertical refresh resulting in smooth animations.See alsoAnimatorUpdater, VBlankAnimatorUpdater