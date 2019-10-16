Title: Setting up Email with Gandi
Date: 2019-10-16T04:12+00:00
Category: Computers
Tags: Software, Internet
Slug: email-with-gandi

I decided this past weekend to set up my on own domain. My [previous post][1]
detailed why I decided to do this. Now I'll explain how I implented it and why
I made some of the choices that I did.

My DNS is registered using [Gandi][2], and they provide quite an excellent
email hosting solution for their DNS customers. It was extremely easy to set
up, and the details of how can be found [here][3]. A brief summary of how it
works:

1.  You ensure that your [MX records][4] direct mail to Gandi's managed mail
    servers. My domain has the MX records set automatically, but I had to
    manually implement the SPF record.

2.  You purchase some email addresses under your DNS address. Gandi provides
    two offerings - 3GB of storage, or 50GB of storage.

3.  You activate the mailboxes (ie. set the username and password for the
    purchased account(s)).

Here are some of the reasons I like this approach and some of the features I
like about this setup:

*   I don't have to manage the mail server myself. This saves me the effort of
    having to set up a mail transfer agent, IMAP server, web interface, spam
    filter, and so on.

*   It supports an unlimited number of aliases. This is great for all those
    web services that require registration so they can send you lots of spam
    later on. Simply create a new alias and register with that, then if you
    want to stop receiving their messages, you can delete the alias! And if
    you want to re-enable it, you can simply add it back, temporarily or
    permanently.

*   It comes with a built-in webmail interface, but IMAP is trivial to set up
    as well.

*   It's a small step for freedom from the large internet companies that now
    serve the majority of email, nay, all of our internet communications.

The major drawback of this setup is that I am still not *hosting* the mail
myself. Doing so would require a lot of independent work, though that's not a
drawback in and of itself. However, since incoming mail will always be
addressed to the current domain, should I change my mind and self-host at some
later date, I can still use the same mail addresses that I set up with the
provider's managed solution.

That's it! I was surprised at how easy it was and I'm loving this solution.
Hopefully I'll be able to start migrating some of my accounts to use these new
addresses.

[1]: email-on-your-own-domain.html
[2]: https://www.gandi.net/
[3]: https://docs.gandi.net/en/gandimail/index.html
[4]: https://docs.gandi.net/en/gandimail/common_operations/create_email_address.html#check-for-correct-mx-records
