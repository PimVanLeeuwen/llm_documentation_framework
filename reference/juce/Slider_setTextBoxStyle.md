#### setTextBoxStyle()


 void Slider::setTextBoxStyle ( TextEntryBoxPosition newPosition, 
 
 bool isReadOnly, 
 int textEntryBoxWidth, 
 int textEntryBoxHeight ) 

Changes the location and properties of the textentry box.Parameters

 newPosition where it should go (or NoTextBox to not have one at all) 
 
 isReadOnly if true, it's a readonly display 
 textEntryBoxWidth the width of the textbox in pixels. Make sure this leaves enough room for the slider as well! 
 textEntryBoxHeight the height of the textbox in pixels. Make sure this leaves enough room for the slider as well! 



See alsosetTextBoxIsEditable, getValueFromText, getTextFromValue