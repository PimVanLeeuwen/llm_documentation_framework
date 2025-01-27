#### setExpanded()


 void MultiChoicePropertyComponent::setExpanded ( bool expanded ) noexcept 
 

Expands or shrinks the list of options if they are not all visible.N.B. This will just set the preferredHeight value of the PropertyComponent and attempt to call PropertyPanel::resized(), so if you are not displaying this object in a PropertyPanel then you should use the onHeightChange callback to resize it when the height changes.See alsoonHeightChange