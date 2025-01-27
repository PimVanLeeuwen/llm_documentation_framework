#### withTimeTransform()


 AnimatorSetBuilder AnimatorSetBuilder::withTimeTransform ( std::function< double(double)> transform ) 
 

Specifies a time transformation function that the built Animator should utilise, allowing accelerating and decelerating the entire set of Animators.The provided function should be monotonically increasing.