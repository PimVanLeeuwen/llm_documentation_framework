#### isEnabled()


 bool Component::isEnabled ( ) const noexcept 
 

Returns true if the component (and all its parents) are enabled.Components are enabled by default, and can be disabled with setEnabled(). Exactly what difference this makes to the component depends on the type. E.g. buttons and sliders will choose to draw themselves differently, etc.Note that if one of this component's parents is disabled, this will always return false, even if this component itself is enabled.See alsosetEnabled, enablementChanged