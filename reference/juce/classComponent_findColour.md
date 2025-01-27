#### findColour()


 Colour Component::findColour ( int colourID, 
 
 bool inheritFromParent = false ) const 

Looks for a colour that has been registered with the given colour ID number.If a colour has been set for this ID number using setColour(), then it is returned. If none has been set, the method will try calling the component's LookAndFeel class's findColour() method. If none has been registered with the lookandfeel either, it will just return black.The colour IDs for various purposes are stored as enums in the components that they are relevant to for an example, see Slider::ColourIds, Label::ColourIds, TextEditor::ColourIds, TreeView::ColourIds, etc.See alsosetColour, isColourSpecified, colourChanged, LookAndFeel::findColour, LookAndFeel::setColour