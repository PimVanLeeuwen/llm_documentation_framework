#### addDefaultKeypress()


 void ApplicationCommandInfo::addDefaultKeypress ( int keyCode, ModifierKeys modifiers ) noexcept 
 

Handy method for adding a keypress to the defaultKeypresses array.This is just so you can write things like:myinfo.addDefaultKeypress ('s', ModifierKeys::commandModifier);
ModifierKeys::commandModifier@ commandModifierCommand key flag on windows this is the same as the CTRL key flag.Definition juce\_ModifierKeys.h:152
instead ofmyinfo.defaultKeypresses.add (KeyPress ('s', ModifierKeys::commandModifier));
KeyPressRepresents a key press, including any modifier keys that are needed.Definition juce\_KeyPress.h:52


Member Data Documentation