Twitter Sort-Response
==========

Twitter Sort-Response responds to the dire need of the general twittersphere 
with their sorting dilema. It is a response to [Twitter Sort](https://github.com/ExPHAT/twitter-sort) by ExPHAT.

Setup
-----
Ensure you have the `tweepy` module installed:

    pip install tweepy

    OR

    sudo easy_install tweepy

Or clone from the Git repository:

    git clone https://github.com/tweepy/tweepy.git
    cd tweepy
    python setup.py install

Rename `example.settings.py` to `settings.py` and fill the required attributes.

If you want to use notifications, then run

```shell
[sudo] gem install terminal-notifier
```

And use the --notify flag

Usage
-----

```shell
$ python main.py [--notify]
```
