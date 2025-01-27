#### fadeOut()


 void ComponentAnimator::fadeOut ( Component \* component, 
 
 int millisecondsToTake ) 

Begins a fadeout of this components alpha level.This is a quick way of invoking animateComponent() with a target alpha value of 0.0f, using a proxy. You're safe to delete the component after calling this method, and this won't interfere with the animation's progress.