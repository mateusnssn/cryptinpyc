<!--
<div align="center">
 <img src="./archive-repository.svg" width="30%">
</div>

-->

# cryptinpyc
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

Use this repository to encrypt texts.

**:warning: Please, do not use this code for serious and confidential purposes. Encrypted data does not follow recommended data protection standards.** 

Among the various problems, the main vulnerabilities are:
* character frequency decoding;
* brute force decoding.

Feel free to implement solutions to this.

 
## Architecture

 #### Modularization by files:
|Archive|function|
|---|---|
| [`./app/calc.py`](./app/calc.py) | Contains some relevant math functions |
|[`./app/console.py`](./app/console.py)|Program management apparatus|
|[`./app/gfile.py`](./app/gfile.py)|Create and write generated results to disk|
|[`./app/read.py`](./app/read.py)|Reads and converts encoded data|
|[`./app/RSA/conversion.py`](./app/RSA/conversion.py)|translate the data|
|[`./app/RSA/gk.py`](./app/RSA/gk.py)|Generates keys (public and private)|
|[`./app/RSA/main.py`](./app/RSA/main.py)|Performs encryption based on generated keys|
|[`./app/RSA/preCoding.py`](./app/RSA/preCoding.py)|Unicode translation with its correspondent |
|[`./app/.glp/glp.c`](./app/.glp/glp.c) e [`./app/.glp/glp.py`](./app/.glp/glp.py)|Apparatus for creating the list of prime numbers [lp.txt](./app/.glp/lp.txt)|
|[`./app/.glp/glp.sh`](./app/.glp/glp.sh)|Writes prime numbers found |

 

## How to use:

So that you can interact with the program there is the [console.py](./app/console.py) file, which can be run from the CLI and has a built-in help guide. It's important that you are in the `app` directory so that nothing unexpected happens.
 ```
$ python3 console.py
 ```
You can encrypt data and it will be saved in a randomly named folder containing the files: 
 * `ief` (dados criptografados); 
 * `pb` (chave pública);
 * `pv` (chave privada).
 
 **:warning: The `pv` file must be removed from the directory if you want to send the folder confidentially to someone.**


## Para contribuir:

1. Faça um fork do projeto;
2. Clone o projeto do seu fork (`git clone https://github.com/SEU_USUARIO/cryptinpyc.git`) **(não se esqueça de mudar SEU_USUÁRIO no link)**;
3. Crie sua branch para realizar sua modificação (`git checkout -b feature/NOME_DA_MODIFICAÇÃO`);
4. Após ter realizado suas modificações, faça um commit (`git commit -m "DESCRIÇÃO_DA_MODIFICAÇÃO"`);
5. Faça o Push para seu repositório (`git push origin feature/NOME_DA_MODIFICAÇÃO`);
6. No seu repositório no Github crie uma Pull Request para que seja avaliada a suas modificações para ser feito o merge no projeto principal.

<br>
<hr>
<p align="center">
made with ♥ by a student
<p/>

