# Password Manager
A basic password manager utility that allows a user to encrypt passwords under a master password.


## Usage steps
The user creates a file named "passwords.txt" (The name of the file the program uses can be changed by modifying the code).
The first line of the file contains a list of passwords and the passwords are stored on subsequent lines.
The user then can encrypt this file running encrypt_decrypt2.0.py, with options to encrypt, decrypt, or remove the passwords.txt file.
When encrypting, the user must create a master password and confirm it by typing it again.
A encrypted file called "encrypted.txt" is created and the "passwords.txt" file is overwritten multiple times and then deleted.
To decrypt the file, the master password is required, and a "passwords.txt" file is regenerated from the encrypted file.


## "Known Answer Tests" (KATs) a.k.a. test vectors
There are five KATs in the repo.
Each KAT contains a passwords.txt file, an encrypted.txt file, and a parameters.txt file which lists the parameters used.
The parameters are:
- GLOBAL_LENGTH: This is set in encrypt_decrypt2.0.py, and is equivalent to the line length in encrypted.txt.
- LOOPS: This is set in encrypt_decrypt2.0.py.
The processing power required to encrypt/decrypt or attempt a brute force attack scales approximately linearly with this value.
- Master Password: The master password used to encrypt or decrypt.

KAT1 contains a simple example.
KAT2 contains an example of the resulting "passwords.txt" file regenerated from the same encrypted file as KAT1,
but using a slightly incorrect master password. The resulting "passwords.txt" file is significantly different (and incorrect relative to KAT1).
KAT3 contains an example of the resulting "passwords.txt" file regenerated from the same encrypted file as KAT1,
but using a different LOOPS parameter. The resulting "passwords.txt" file is significantly different (and incorrect relative to KAT1).
KAT4 contains an example of the resulting "encrypted.txt" file generated from the same "passwords.txt" file as KAT1,
but with a different password. The resulting "encrypted.txt" file is significantly different.
KAT5 contains an example of the resulting "encrypted.txt" file generated from the same "passwords.txt" file as KAT1,
but with a slightly different password of the same length. The resulting "encrypted.txt" file is significantly different.


## Security
The encryption scheme uses the modulus of SHA-256 (of the SHA-2 standard) hashes to secure the passwords.
Therefore the security of the scheme relies in part on the security of SHA-2.

One concern is that if passwords are added and the same master password is used to encrypt, an attacker can gain information if they
have access to the original encrypted file and the new encrypted file.

A positive point on the security is that practically speaking, any guess at the master password can "unencrypt" the encrypted file.
However, only the correct master password gives the correct unencrypted file.
Therefore, it can be quite difficult for an attacker to distinguish between the correct master password and incorrect master passwords.

Side channel attacks on the encryption phase can reveal information about the parameters used and information about the master password.
Side channel attacks on the decryption phase can additionally reveal information on the length of passwords.


## Compatibility
Written and tested for python 2.7 on Windows.
Needs minor changes for python 3 (e.g. replace uses of raw_input).
May have compatibility issues on other platforms.