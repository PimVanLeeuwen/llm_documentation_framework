#### getAnimator()


 ComponentAnimator & Desktop::getAnimator ( ) noexcept 
 

The ComponentAnimator has been superseded, it is now recommended you use the Animator class in the juce\_animation module.The Desktop object has a ComponentAnimator instance which can be used for performing your animations.Having a single shared ComponentAnimator object makes it more efficient when multiple components are being moved around simultaneously. It's also more convenient than having to manage your own instance of one.See alsoAnimator, ComponentAnimator