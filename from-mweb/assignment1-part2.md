# Assignment1, Part2

> By: Xu Congyu

## Technique I used

First, I used google to determine which kinds of hash algorithm are used.

Then, I found that the leaked password file of yahoo is all plaintext, so I use Python to get Top 10000 passwords in password.file and save it to **password.txt**

I wrote a Python script, picked 100 hashed password in txt file.

* For Linikedin, use hashlib.sha1 to hash password in **password.txt**, and compare them with passwords in **SHA1.txt** one by one.
* For Formspring, add a salt \(from '00' to '99\)' to password in **password.txt**, then compare them with passwords in **formspring.txt** one by one. Because this needs a lot more calculation than that of Linkedin, I used multiprocess to deal with it.

## Other technique I considered

* Goole if there is a plaintext version of leaked database which is decrypted by others.
* Use rainbow table online to decrypt those hashed passwords.

## How were the password stored

> Device: Macbook pro 2015 \(i5, 2.7Ghz\)

* **Yahoo** : passwords are plaintext. No difficulty to crack.
* **Linkedin** : passwords are hashed by SHA1 but many hashes' first 5 letters are replaced by '00000'. The difficulty to crack depends on how good and how big is my wordlist, complexity of passwords and calculation ability of cracker.

  Using top10000 passwords of yahoo as wordlist and **single process**, I can just decrypt about one hashed password in every 1000. it takes **0.641s** to try to crack **100** hashed passwords.

  ```text
    python crack.py  0.61s user 0.01s system 97% cpu 0.641 total
  ```

* **Formspring** " passwords are hashed by SHA256 with salts. The difficulty is similar to Linkedin, but much harder due to its 2-digit salts.

  Using top10000 passwords of yahoo as wordlist and **10 processes**, it takes **427.99s** to try to crack **100** hashed passwords.

  ```text
    python formspring.py  427.99s user 1.83s system 364% cpu 1:57.93 total
  ```

