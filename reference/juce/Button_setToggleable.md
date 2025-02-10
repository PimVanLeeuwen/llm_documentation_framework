#### setToggleable()


 void Button::setToggleable ( bool shouldBeToggleable ) 
 

Indicates that the button's on/off state is toggleable.By default this is false, and will only be true for ToggleButtons, buttons that are a part of a radio button group, and buttons for which getClickingTogglesState() == true, however you can use this method to manually indicate that a button is toggleable.This will present the button as toggleable to accessibility clients and add an accessible "toggle" action for the button that invokes setToggleState().See alsoToggleButton, isToggleable, setToggleState, setClickingTogglesState, setRadioGroupId