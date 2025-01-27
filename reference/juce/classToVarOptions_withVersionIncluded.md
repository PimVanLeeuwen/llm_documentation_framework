#### withVersionIncluded()


 ToVarOptions ToVarOptions::withVersionIncluded ( bool x ) const nodiscard 
 

By default, conversion will include version information for any type with a nonnull marshallingVersion.Setting versionIncluded to false will cause the version info to be omitted, which is useful in situations where the version information is not needed (e.g. when presenting transient information to the user, rather than writing data to disk that must be deserialised in the future).References withMember(), and x.