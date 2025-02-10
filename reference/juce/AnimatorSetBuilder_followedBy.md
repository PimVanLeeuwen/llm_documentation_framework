#### followedBy() [3/3]


 AnimatorSetBuilder AnimatorSetBuilder::followedBy ( std::function< void()> cb ) 
 

Adds an empty Animator to the execution graph that will start executing after the Animator provided last to this builder object, completes upon its first update, and executes the provided callback.