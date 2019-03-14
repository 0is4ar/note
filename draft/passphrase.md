## passphrase

The passphrase is just a key used to encrypt the file that contains the RSA key, using a symmetric cipher (usually DES or 3DES). In order to use the key for public-key encryption, you first need to decrypt its file using the decryption key. ssh does this automatically by asking your for the passphrase


## ssh-add

`ssh-add`adds private key identities (from your`~/.ssh`directory) to the authentication agent (`ssh-agent`), so that the ssh agent can take care of the authentication for you, and you don’t have type in passwords at the terminal.