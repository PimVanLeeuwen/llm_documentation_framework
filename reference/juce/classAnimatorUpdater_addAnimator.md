#### addAnimator() [2/2]


 void AnimatorUpdater::addAnimator ( const Animator & animator, 
 
 std::function< void()> onComplete ) 

Registers an Animator with the updater and specifies a callback to be called upon the completion of the Animator.This callback can be used for cleanup purposes e.g.animatorUpdater.addAnimator (someComponentPtr>getAnimator(),
 [&someComponentPtr] { someComponentPtr.reset(); });