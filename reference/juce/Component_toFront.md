#### toFront()


 void Component::toFront ( bool shouldAlsoGainKeyboardFocus ) 
 

Brings the component to the front of its siblings.If some of the component's siblings have had their 'alwaysontop' flag set, then they will still be kept in front of this one (unless of course this one is also 'alwaysontop').Parameters

 shouldAlsoGainKeyboardFocus if true, this will also try to assign keyboard focus to the component (see grabKeyboardFocus() for more details) 
 



See alsotoBack, toBehind, setAlwaysOnTop