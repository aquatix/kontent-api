kontent-api
===========

JSON-REST backend store for websites. Websites, CMS, apps are clients talking to this API.


## Data model

### ContentObject

meta object for a content entry (like an article, page or something). Contains references to the real items

- creation_date: date/time stamp of first version
- current_date: date/time stamp of latest version
- revisions: List of items, versions of this particular content item


### GenericItem

generic content item, specific types inherit from this

- revision_date
- title
- authors: List of Author
- privacy_state: private/public/?
- tags: List of Tags


### TextItem

extends GenericItem

- body_text: 'raw' text of the item
- body_text_type: 
- external_link: url to external source. Can be used to point to a related article on another site or as a blogmark, for example


### ImageItem

- mimetype
- url
- width
- height
- size: size of original file in bytes

An ImageItem has functions to return resized versions of the image, possibly in another format (png, jpg, gif etc)


### BinaryItem

generic attachment-like item

- mimetype
- url
- size: size of file in bytes


### Tag

- name
- slug

Tags also function as classical categories


### TextType

kinds of content a textfield can contain and their parsers which can output various types of formats. Markdown can be converted to HTML, HTML to plain text etc

- Markdown
- BBU
- Pure html
- Plaintext (might be marked up as monospace in a client, for example)


### Author

user object. Just make this a User?

- name
- email
