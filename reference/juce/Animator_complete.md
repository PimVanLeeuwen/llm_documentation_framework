#### complete()


 void Animator::complete ( ) const 
 

Marks the Animator ready to be completed.ValueAnimators will be completed automatically when they reach a progress >= 1.0 unless they are infinitely running. AnimatorSets will also complete on their own when all of their constituent Animators complete.Using this function you can fast track the completion of an Animator. After calling this function isComplete will return true, and it's guaranteed that you will receive an update callback with a progress value of 1.0. After this the onComplete callback will be executed.