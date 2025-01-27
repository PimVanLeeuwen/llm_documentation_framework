#### setBroughtToFrontOnMouseClick()


 void Component::setBroughtToFrontOnMouseClick ( bool shouldBeBroughtToFront ) noexcept 
 

Indicates whether the component should be brought to the front when clicked.Setting this flag to true will cause the component to be brought to the front when the mouse is clicked somewhere inside it or its child components.Note that a toplevel desktop window might still be brought to the front by the operating system when it's clicked, depending on how the OS works.By default this is set to false.See alsosetMouseClickGrabsKeyboardFocus