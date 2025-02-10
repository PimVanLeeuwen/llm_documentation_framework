#### animateComponent()


 void ComponentAnimator::animateComponent ( Component \* component, 
 
 const Rectangle< int > & finalBounds, 
 float finalAlpha, 
 int animationDurationMilliseconds, 
 bool useProxyComponent, 
 double startSpeed, 
 double endSpeed ) 

Starts a component moving from its current position to a specified position.If the component is already in the middle of an animation, that will be abandoned, and a new animation will begin, moving the component from its current location.The start and end speed parameters let you apply some acceleration to the component's movement.Parameters

 component the component to move 
 
 finalBounds the destination bounds to which the component should move. To leave the component in the same place, just pass component>getBounds() for this value 
 finalAlpha the alpha value that the component should have at the end of the animation 
 animationDurationMilliseconds how long the animation should last, in milliseconds 
 useProxyComponent if true, this means the component should be replaced by an internally managed temporary component which is a snapshot of the original component. This avoids the component having to paint itself as it moves, so may be more efficient. This option also allows you to delete the original component immediately after starting the animation, because the animation can proceed without it. If you use a proxy, the original component will be made invisible by this call, and then will become visible again at the end of the animation. It'll also mean that the proxy component will be temporarily added to the component's parent, so avoid it if this might confuse the parent component, or if there's a chance the parent might decide to delete its children. 
 startSpeed a value to indicate the relative start speed of the animation. If this is 0, the component will start by accelerating from rest; higher values mean that it will have an initial speed greater than zero. If the value is greater than 1, it will decelerate towards the middle of its journey. To move the component at a constant rate for its entire animation, set both the start and end speeds to 1.0 
 endSpeed a relative speed at which the component should be moving when the animation finishes. If this is 0, the component will decelerate to a standstill at its final position; higher values mean the component will still be moving when it stops. To move the component at a constant rate for its entire animation, set both the start and end speeds to 1.0