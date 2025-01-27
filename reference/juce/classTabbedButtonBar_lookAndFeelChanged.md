#### lookAndFeelChanged()


 void TabbedButtonBar::lookAndFeelChanged ( ) overridevirtual 
 

Called to let the component react to a change in the lookandfeel setting.When the lookandfeel is changed for a component, this method, repaint(), and colourChanged() are called on the original component and all its children recursively.It can also be triggered manually by the sendLookAndFeelChange() method, in case an application uses a LookAndFeel class that might have changed internally.See alsosendLookAndFeelChange, getLookAndFeel Reimplemented from Component.