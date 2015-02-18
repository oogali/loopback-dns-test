# Loopback DNS Test

> Engineers are really good at labeling and branding things. If we had named Kentucky Fried Chicken, it would have been Hot Dead Birds.

> -- Vint Cerf

## Introduction

This is just the result of me playing around with the idea of building a very simple DNS server in Python.

Any DNS query you throw at it, it will respond with an A record pointing you to 127.0.0.1.

## Running

### Preparing

You know virtualenv, right? It's optional, but highly recommended.

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    
If you choose not to use virtalenv, this is for you:

    $ sudo pip install -r requirements.txt

### Running the tool

    $ ./loopback-dns.py

And that's it. It should print out every DNS query it receives.
