#### setAllowedPlacement()


 void BubbleComponent::setAllowedPlacement ( int newPlacement ) 
 

Tells the bubble which positions it's allowed to put itself in, relative to the point at which it's pointing.By default when setPosition() is called, the bubble will place itself either above, below, left, or right of the target area. You can pass in a bitwise'or' of the values in BubblePlacement to restrict this choice.E.g. if you only want your bubble to appear above or below the target area, use setAllowedPlacement (above below);See alsoBubblePlacement