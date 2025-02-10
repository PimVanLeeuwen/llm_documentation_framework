#### getLookAndFeel()


 LookAndFeel & Component::getLookAndFeel ( ) const noexcept 
 

Finds the appropriate lookandfeel to use for this component.If the component hasn't had a lookandfeel explicitly set, this will return the parent's lookandfeel, or just the default one if there's no parent.See alsosetLookAndFeel, lookAndFeelChanged Referenced by LassoComponent< SelectableItemType >::paint(), and StandalonePluginHolder::showAudioSettingsDialog().