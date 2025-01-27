#### start()


 void Animator::start ( ) const 
 

Marks the Animator ready for starting.You must call this function to allow the Animator to move out of the idle state.After calling this function the Animator's on start callback will be executed at the next update immediately followed by the first call to it's update function.You can call this function before or after adding the Animator to an AnimatorUpdater. Until start() is called the Animator will just sit idly in the updater's queue.