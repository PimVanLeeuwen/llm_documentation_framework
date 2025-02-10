#### setComponentEffectForBubbleComponent()


 void LookAndFeel\_V2::setComponentEffectForBubbleComponent ( BubbleComponent & bubbleComponent ) overridevirtual 
 

Override this method to set effects, such as a dropshadow, on a BubbleComponent.This will be called whenever a BubbleComponent is constructed or its lookandfeel changes.If you need to trigger this callback to update an effect, call sendLookAndFeelChange() on the component.See alsoComponent::setComponentEffect, Component::sendLookAndFeelChange Implements BubbleComponent::LookAndFeelMethods.