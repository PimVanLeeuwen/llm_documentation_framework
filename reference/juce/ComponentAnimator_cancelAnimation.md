#### cancelAnimation()


 void ComponentAnimator::cancelAnimation ( Component \* component, 
 
 bool moveComponentToItsFinalPosition ) 

Stops a component if it's currently being animated.If moveComponentToItsFinalPosition is true, then the component will be immediately moved to its destination position and size. If false, it will be left in whatever location it currently occupies.