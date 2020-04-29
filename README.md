scrapy-firebase
===============
Firebase pipeline for Scrapy.

Installation
------------
Install via `pip`:

    pip install scrapy-firebase

Configuration
-------------

### Basic configuration example


Add `scrapy-firebase` to your projects `settings.py` file and setup some variables.

```python
ITEM_PIPELINES = [
  'scrapy_firebase.FirebasePipeline',
]

FIREBASE_CERTIFICATE = 'path to certificate.json'

# Replace project-id to yours.
FIREBASE_DATABASE = 'https://project-id.firebaseio.com/'

# Insert an appropriate value.
FIREBASE_REF = ''

# To compose more robust child paths, you can add a list of properties.
FIREBASE_KEYS = ['uid', 'spider_name']

```
