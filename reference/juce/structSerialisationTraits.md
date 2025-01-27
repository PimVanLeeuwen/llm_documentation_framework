template<typename T>
struct SerialisationTraits< T >Allows serialisation functions to be attached to a specific type without having to modify the declaration of that type.A specialisation of SerialisationTraits must include:A static constexpr data member named 'marshallingVersion' with a value that is convertible to std::optional<int>.Either:Normally, a single function with the following signature: template <typename Archive, typename Item>
static void serialise (Archive& archive, Item& item);
For types that must do slightly different work when loading and saving, you may supply two functions with the following signatures, where "T" is a placeholder for the type on which SerialisationTraits is specialised: template <typename Archive>
static void load (Archive& archive, T& item);
 
template <typename Archive>
static void save (Archive& archive, const T& item);
If the marshallingVersion converts to a null optional, then all versioning information will be ignored when marshalling the type. Otherwise, if the value converts to a nonnull optional, this versioning information will be included when serialising the type.Inside serialise() and load() you may call archive.getVersion() to find the detected version of the object being deserialised. archive.getVersion() will return an std::optional<int>, where 'nullopt' indicates that no versioning information was detected.Marshalling functions can also be specified directly inside the type to be marshalled. This approach may be preferable as it is more concise. Internal marshalling functions are written in exactly the same way as external ones; i.e. the type must include a marshallingVersion, and either a single serialise function, or a load/save pair of functions, as specified above.The documentation for this struct was generated from the following file:juce\_Serialisation.h
### Purchase

Get JUCE
### Discover

What's New in JUCEFeatures
### Learn

DocumentaionTutorialsMade with JUCEResources
### Support

JUCE ForumNewsletterArchive
### About

Contact UsJUCE LegalJUCE Licensing FAQ
### Events

Audio Developer Conference
Visit our FacebookVisit our TwitterVisit our LinkedInVisit our YouTube channel© Raw Material Software Limited
linkedin




facebook


pinterest


youtube


rss


twitter


instagram




facebookblank


rssblank


linkedinblank


pinterest


youtube


twitter


instagram