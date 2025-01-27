#### withParentComponent()


 MessageBoxOptions MessageBoxOptions::withParentComponent ( Component \* component ) const nodiscard 
 

The component that will contain the message box (e.g.the AudioProcessorEditor in a plugin).This will only affect JUCE AlertWindows. It won't affect the drawing of native message boxes. This is mainly intended for use in AU plugins, where opening additional windows can be problematic.References withMember().