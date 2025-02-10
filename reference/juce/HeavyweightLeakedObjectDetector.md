template<class OwnerClass>
class HeavyweightLeakedObjectDetector< OwnerClass >This class is a useful way of tracking down hard to find memory leaks when the regular LeakedObjectDetector isn't enough.As well as firing when any instances of the OwnerClass type are leaked, it will print out a stack trace showing where the leaked object was created. This is obviously quite a heavyweight task so, unlike the LeakedObjectDetector which should be always be added to your classes, you should only use this object temporarily when you are debugging and remove it when finished.To use it, use the JUCE\_HEAVYWEIGHT\_LEAK\_DETECTOR macro as a simple way to put one in your class declaration.

Constructor & Destructor Documentation


◆ HeavyweightLeakedObjectDetector() [1/2]


template<class OwnerClass > 

 HeavyweightLeakedObjectDetector< OwnerClass >::HeavyweightLeakedObjectDetector ( ) noexcept 
 

References SystemStats::getStackBacktrace().

◆ HeavyweightLeakedObjectDetector() [2/2]


template<class OwnerClass > 

 HeavyweightLeakedObjectDetector< OwnerClass >::HeavyweightLeakedObjectDetector ( const HeavyweightLeakedObjectDetector< OwnerClass > & ) noexcept 
 

References SystemStats::getStackBacktrace().

◆ ~HeavyweightLeakedObjectDetector()


template<class OwnerClass > 

 HeavyweightLeakedObjectDetector< OwnerClass >::~HeavyweightLeakedObjectDetector ( ) 
 