# Hosting Block Explorer

## Install and run the Qwertycoin daemon on your server

You can install the Qwertycoin daemon from precompiled sources or compile it yourself. Guides for both are below.

### Precompiled

* You can download the precompiled binaries [here](https://releases.qwertycoin.org/). Enter your downloaded file through your terminal and run `qwertycoind` with an open port like so:

```text
./qwertycoind --restricted-rpc --enable-cors=* --enable-blockchain-indexes --rpc-bind-ip=0.0.0.0 --rpc-bind-port=8197
```

### Compile yourself

* This is a guide for compiling on Linux \(Ubuntu\). For other operating systems you can find a guide [here](https://github.com/qwertycoin-org/qwertycoin#windows-10-).

#### Install dependancies

```text
sudo apt-get install build-essential cmake git
```

* You will need Cmake version 3.10 to compile Qwertycoin. You can find a guide on installing that [here](https://docs.qwertycoin.org/developer/developer/fixes/Install-Cmake-3.10).

#### Building

* After installing the dependencies you can run this simple script:

```text
git clone --recurse-submodules https://github.com/qwertycoin-org/qwertycoin
cd ./qwertycoin
mkdir ./build
cd ./build
cmake -DBUILD_ALL:BOOL=TRUE ..
cmake --build . --config Release
```

* If all went well, it will complete successfully, and you will find all your binaries in the `./build/src` directory.
* Finally run `qwertycoind` with an open port like so:

```text
./qwertycoind --restricted-rpc --enable-cors=* --enable-blockchain-indexes --rpc-bind-ip=0.0.0.0 --rpc-bind-port=8197
```

## Install the block explorer code

You can host the block explorer with Apache or Nginx. For this guide I will be using Apache.

* Install Apache

```text
sudo apt-get update

sudo apt-get install apache2

sudo ufw allow 'Apache Full'
```

* Next download the block explorer code

```text
git clone https://github.com/qwertycoin-org/qwertycoin-blockchain-explorer.git
```

* Change the 'api' variable in config.js to point to your daemon. Also change the '$apiNode=' variable in /api/index.php to point the API urls to your daemon.
* Once that is done copy all the files to the html directory.

```text
sudo cp -rf api/ config.js css/ favicon.ico index.html js/ LICENSE pages/ q/ README.md /var/www/html/
```

* Your block explorer can now be seen at your servers address.

Extra:

* You can change the look of your block explorer by playing around with the `css` files.

_Last updated on 2020-2-16_

* [Install and run the Qwertycoin daemon on your server]()
  * [Precompiled]()
  * [Compile yourself]()
* [Install the block explorer code]()

