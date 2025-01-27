#### compareAndSetBool()


template<typename Type > 

 bool Atomic< Type >::compareAndSetBool ( Type newValue, Type valueToCompare ) noexcept 
 

Atomically compares this value with a target value, and if it is equal, sets this to be equal to a new value.This operation is the atomic equivalent of doing this:bool compareAndSetBool (Type newValue, Type valueToCompare)
{
 if (get() == valueToCompare)
 {
 set (newValue);
 return true;
 }
 
 return false;
}
Atomic::setvoid set(Type newValue) noexceptAtomically sets the current value.Definition juce\_Atomic.h:82
Atomic::compareAndSetBoolbool compareAndSetBool(Type newValue, Type valueToCompare) noexceptAtomically compares this value with a target value, and if it is equal, sets this to be equal to a ne...Definition juce\_Atomic.h:111
Atomic::getType get() const noexceptAtomically reads and returns the current value.Definition juce\_Atomic.h:79
Internally, this method calls std::atomic::compare\_exchange\_strong with memory\_order\_seq\_cst (the strictest std::memory\_order).Returnstrue if the comparison was true and the value was replaced; false if the comparison failed and the value was left unchanged. 
See alsocompareAndSetValue References Atomic< Type >::value.Referenced by ThreadLocalValue< Type >::get().