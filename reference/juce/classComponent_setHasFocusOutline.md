#### setHasFocusOutline()


 void Component::setHasFocusOutline ( bool hasFocusOutline ) noexcept 
 

Use this to indicate that the component should have an outline drawn around it when it has keyboard focus.If this is set to true, then when the component gains keyboard focus the LookAndFeel::createFocusOutlineForComponent() method will be used to draw an outline around it.See alsoFocusOutline, hasFocusOutline