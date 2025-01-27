#### paintButton()


 virtual void Button::paintButton ( Graphics & g, bool shouldDrawButtonAsHighlighted, bool shouldDrawButtonAsDown ) protectedpure virtual 
 

Subclasses should override this to actually paint the button's contents.It's better to use this than the paint method, because it gives you information about the over/down state of the button.Parameters

 g the graphics context to use 
 
 shouldDrawButtonAsHighlighted true if the button is either in the 'over' or 'down' state 
 shouldDrawButtonAsDown true if the button should be drawn in the 'down' position 


Implemented in ArrowButton, DrawableButton, HyperlinkButton, ImageButton, ShapeButton, TabBarButton, TextButton, ToggleButton, and ToolbarItemComponent.