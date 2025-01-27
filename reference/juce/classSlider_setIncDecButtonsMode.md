#### setIncDecButtonsMode()


 void Slider::setIncDecButtonsMode ( IncDecButtonMode mode ) 
 

When the style is IncDecButtons, this lets you turn on a mode where the mouse can be dragged on the buttons to drag the values.By default this is turned off. When enabled, clicking on the buttons still works them as normal, but by holding down the mouse on a button and dragging it a little distance, it flips into a mode where the value can be dragged. The drag direction can either be set explicitly to be vertical or horizontal, or can be set to incDecButtonsDraggable\_AutoDirection so that it depends on whether the buttons are sidebyside or above each other.