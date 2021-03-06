kontent-api
===========

JSON-REST backend store for websites. Websites, CMS, apps are clients talking to this API.


## Setup

Clone the repository and be sure you have virtualenv installed (`python-virtualenv` on .deb-based distro's). Then create a virtualenv for this project (in the example called `kontentenv` but you can call it whatever you want):

```
virtualenv kontentenv
source kontentenv/bin/activate

# now go into our source tree and install the dependencies:
cd kontent-api
pip install -r requirements.txt

# create a database (sqlite for now):
cd kontent
python manage.py syncdb
```


## Data model

### KontentUser

user object; inherits from User? OneToOne?

- User (Django auth user)
- name
- email
- role: commenter, editor, admin


### Site

site instance. The backend supports multiple sites

- title
- creation_date: date/time stamp
- owner: KontentUser (more to denote who to address; right management is done through Django user management)
- protected: boolean, denotes whether someone has to login to view (ACL?)


### ContentGroup

filter on ContentObject to serve as category overview, for example (by filtering on certain tag, part of title, content type, etc)

- site: Site (the site instance this group belongs to)
- filter: Filter
- parent: ContentGroup (None or top, otherwise its parent in a tree of groups)
- protected: boolean, denotes whether someone has to login to view (ACL?)


### ContentObject

meta object for a content entry (like an article, page or something). Contains references to the real items

- site: Site (the site instance this group belongs to)
- creation_date: date/time stamp of first version
- current_date: date/time stamp of latest version
- revisions: List of items, versions of this particular content item
- protected: boolean, denotes whether someone has to login to view (ACL?)


### GenericItem

generic content item, specific types inherit from this

- site: Site (the site instance this item belongs to)
- revision_id: integer with version of this particular instance
- revision_date: date/time stamp of this revision
- title
- authors: List of KontentUser
- is_public: Boolean, denoting whether item is private or public
- is_published: Boolean, denoting whether item has been published or (still) draft
- tags: List of Tag


### TextItem

extends GenericItem

- body_text: 'raw' text of the item
- body_text_type: 
- external_link: url to external source. Can be used to point to a related article on another site or as a blogmark, for example


### ImageItem

extends GenericItem

- mimetype
- url
- width
- height
- size: size of original file in bytes

An ImageItem has functions to return resized versions of the image, possibly in another format (png, jpg, gif etc)


### BinaryItem

extends GenericItem. Generic attachment-like item

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
- UBB (The Ultimate Bulletin Board markup)
- Pure html
- Plaintext (might be marked up as monospace in a client, for example)


### Filter

filter object for grouping ContentObjects

- title
- type: Tag/search (regexp on title, content or something)


### Comment

Allow anonymous? As in, non-user? Lets do that for the time being

- parent: ContentObject at which is commented
- name
- email
- body
