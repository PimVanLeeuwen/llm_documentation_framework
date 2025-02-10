template<typename ValueType>
class ScopedValueSetter< ValueType >Helper class providing an RAIIbased mechanism for temporarily setting and then resetting a value.E.g.int x = 1;
 
{
 ScopedValueSetter setter (x, 2);
 
 // x is now 2
}
 
// x is now 1 again
 
{
 ScopedValueSetter setter (x, 3, 4);
 
 // x is now 3
}
 
// x is now 4
ScopedValueSetterHelper class providing an RAIIbased mechanism for temporarily setting and then resetting a value.Definition juce\_ScopedValueSetter.h:70
xfloat xDefinition juce\_UnityPluginInterface.h:200
 

Constructor & Destructor Documentation


◆ ScopedValueSetter() [1/2]


template<typename ValueType > 

 ScopedValueSetter< ValueType >::ScopedValueSetter ( ValueType & valueToSet, 
 
 ValueType newValue ) 

Creates a ScopedValueSetter that will immediately change the specified value to the given new value, and will then reset it to its original value when this object is deleted.

◆ ScopedValueSetter() [2/2]


template<typename ValueType > 

 ScopedValueSetter< ValueType >::ScopedValueSetter ( ValueType & valueToSet, 
 
 ValueType newValue, 
 ValueType valueWhenDeleted ) 

Creates a ScopedValueSetter that will immediately change the specified value to the given new value, and will then reset it to be valueWhenDeleted when this object is deleted.

◆ ~ScopedValueSetter()


template<typename ValueType > 

 ScopedValueSetter< ValueType >::~ScopedValueSetter ( ) 
 