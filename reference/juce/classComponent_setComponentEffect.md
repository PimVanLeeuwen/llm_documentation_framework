#### setComponentEffect()


 void Component::setComponentEffect ( ImageEffectFilter \* newEffect ) 
 

Adds an effect filter to alter the component's appearance.When a component has an effect filter set, then this is applied to the results of its paint() method. There are a few preset effects, such as a dropshadow or glow, but they can be userdefined as well.The effect that is passed in will not be deleted by the component the caller must take care of deleting it.To remove an effect from a component, pass a null pointer in as the parameter.See alsoImageEffectFilter, DropShadowEffect, GlowEffect