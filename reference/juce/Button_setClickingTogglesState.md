#### setClickingTogglesState()


 void Button::setClickingTogglesState ( bool shouldAutoToggleOnClick ) noexcept 
 

This tells the button to automatically flip the toggle state when the button is clicked.If set to true, then before the clicked() callback occurs, the togglestate of the button is flipped. This will also cause isToggleable() to return true.See alsoisToggleable