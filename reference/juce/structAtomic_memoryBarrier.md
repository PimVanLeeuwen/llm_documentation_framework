#### memoryBarrier()


template<typename Type > 

 void Atomic< Type >::memoryBarrier ( ) noexcept 
 

Implements a memory read/write barrier.Internally this calls std::atomic\_thread\_fence with memory\_order\_seq\_cst (the strictest std::memory\_order).

Member Data Documentation