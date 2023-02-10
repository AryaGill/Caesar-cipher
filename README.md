# Caesar Cipher
 A CLI tool built with Python 3 designed to encrypt, decrypt, and brute force Caesar Cipher.
 
## Usage
 * First type ```python3 CaesarCipher.py```in your terminal and then choose your desired arguments.
 * Your first argument should be your chosen mode. ```-d```(decrypt mode), ```-b```(brute force mode), or ```-e```(encrypt mode).
 * This should be followed by the flag ```-t``` and text in quotes after it. The content of the text will depend your mode. plaintext for ```-e``` (encrypt mode), and ecrypted text by Caesar Cipher for ```-d``` (decrypt) or ```-b```(brute force mode).
 * Your last option is ```-k```(key). This is required for all modes except for ```-b```(bruteforce mode) where the all possible values for key are used. 
 * Use ```python3 CaesarCipher.py -h``` for a description of all arguments. See **Arguments** section for more details and a screenshot. 
 

 
### &ensp;Requirements
  * One option from ```-d```, ```-b```, and ```-e``` is required. 
  * ```-t``` followed by text in quotes is alwas required.
  * ```-k``` is required for ```-d``` and ```-e```.
  

 
 
 ## Arguments
 usage: CaesarCipher.py [-h] [-d] [-b] [-e] [-t --text] [-k --key]

options:
  -h, --help  &ensp; show this help message and exit </br>
  &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; -d &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; decryption mode (with known key) </br>
  &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; -b &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; brute force mode (unknown key) </br>
  &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; -e &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; encryption mode </br>
  &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; -t, --text &ensp;&ensp; Enter encrypted or decrypted text </br>
  &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; -k, --key  &ensp;&ensp; Enter shit (key) value for decryption mode (-d) or encryption mode (-e) </br>
 
<img width="548" alt="Screenshot 2023-02-09 at 5 13 28 PM" src="https://user-images.githubusercontent.com/75190244/217975295-aa2b1b0d-9a7e-46d8-838e-1fd8245d1afd.png">



