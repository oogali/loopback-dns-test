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

    $ sudo ./loopback-dns.py

And that's it. It should print out every DNS query it receives, and respond to the client with
127.0.0.1.

```
dig google.com @localhost

; <<>> DiG 9.8.3-P1 <<>> google.com @localhost
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33184
;; flags: qr rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;google.com.            IN  A

;; ANSWER SECTION:
google.com.     60  IN  A   127.0.0.1

;; Query time: 4 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Wed Feb 18 10:02:23 2015
;; MSG SIZE  rcvd: 44
```
