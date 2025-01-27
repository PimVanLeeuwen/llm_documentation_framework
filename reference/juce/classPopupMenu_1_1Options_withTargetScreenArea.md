#### withTargetScreenArea()


 Options PopupMenu::Options::withTargetScreenArea ( Rectangle< int > targetArea ) const nodiscard 
 

Sets the region of the screen next to which the menu should be displayed.To display the menu next to the mouse cursor use withMousePosition(), which is equivalent to passing the following to this function:Rectangle<int>{}.withPosition (Desktop::getMousePosition())
Desktop::getMousePositionstatic Point< int > getMousePosition()Returns the mouse position.
RectangleManages a rectangle and allows geometric operations to be performed on it.Definition juce\_Rectangle.h:79
Rectangle::withPositionRectangle withPosition(ValueType newX, ValueType newY) const noexceptReturns a rectangle with the same size as this one, but a new position.Definition juce\_Rectangle.h:244
withTargetComponent() will also set the target screen area. If you need a target component and a target screen area, make sure to call withTargetScreenArea() after withTargetComponent().See alsowithMousePosition