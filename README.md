# Python Achieve Mint Client

This is a client library to interact with the Achieve Mint API


## Installation

Set up venv
`python3 -m venv venv/`

Activate venv
`source venv/bin/activate`

Install build to build the library
`pip install build`

Build the .whl and .tar.gz library 
`python -m build`

Install the library to use it
`pip install dist/achievemint-0.x.x.whl`

## Usage

include the client in your project:

```
from achievemint.v1.client import Client

cliet = Client(
    client_id='your_client_id',
    client_secret='your_client_secret',
    url='your_url'
)

client.get_user(100)

```
