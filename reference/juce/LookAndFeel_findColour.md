#### findColour()


 Colour LookAndFeel::findColour ( int colourId ) const noexcept 
 

Looks for a colour that has been registered with the given colour ID number.If a colour has been set for this ID number using setColour(), then it is returned. If none has been set, it will just return Colours::black.The colour IDs for various purposes are stored as enums in the components that they are relevant to for an example, see Slider::ColourIds, Label::ColourIds, TextEditor::ColourIds, TreeView::ColourIds, etc.If you're looking up a colour for use in drawing a component, it's usually best not to call this directly, but to use the Component::findColour() method instead. That will first check whether a suitable colour has been registered directly with the component, and will fallback on calling the component's LookAndFeel's findColour() method if none is found.See alsosetColour, Component::findColour, Component::setColour Referenced by StandalonePluginHolder::showAudioSettingsDialog().