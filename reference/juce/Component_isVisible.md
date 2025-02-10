#### isVisible()


 bool Component::isVisible ( ) const noexcept 
 

Tests whether the component is visible or not.this doesn't necessarily tell you whether this comp is actually on the screen because this depends on whether all the parent components are also visible use isShowing() to find this out.See alsoisShowing, setVisible