Review Board Nickname Authentication
==============

Reviewboard extension for nickname-only (guest-like) authentication

This automatically creates a user based on the username alone if an account with that username doesn't exist.
It also hides the password fields and registration form so only nickname authentication is visible. The only 
accounts which must be accessed with a password are super-user and staff accounts. Since the password field is hidden, 
those users would have to have their password already saved in their browser's password manager or user developer tools
to unhide the password field.

WARNING: Don't use this extension in an installation with reviews you don't want "guests" to mess with.
