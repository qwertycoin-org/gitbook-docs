# Creating a Mining Pool

## Prepare Server

### Create AWS Account

Create an account with [Amazon AWS](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start).

### Setup an Instance

On the home page, click the services tab and then go to compute and click 'EC2'. Once you are there you will chose your region on the top of the page in the header section. Next click the 'Launch Instance' button at the center of the page and then select an AMI. For this tutorial I am using Ubuntu Server 16.04 LTS.

Next you will need to choose an instance type. I am just going to use the t2.large for the tutorial.

You can then skip to step six and under the source tap select my IP.

Next press Review and Launch and then create a new key pair to be able to connect with your instance. Once the instance is live, you can connect to your instance using an SSH through Terminal, PuTTY or similar program.

### SSH into the Instance

1. Download key pair that you created earlier
2. Make sure you are in the same directory as the key and allow permissions

```text
chmod 600 <key-name>.pem
```

1. SSH into instance

```text
ssh -i <key-name>.pem ubuntu@<EC2-IP-Address>
```

### Install Dependancies

```text
sudo apt-get install aptitude
```

```text
sudo aptitude update
```

```text
sudo aptitude install –with-recommends build-essential autotools-dev autoconf automake libcurl3 libcurl4-gnutls-dev git make cmake libssl-dev pkg-config libevent-dev libunbound-dev libminiupnpc-dev doxygen supervisor jq libboost-all-dev htop
```

```text
sudo apt-get install build-essential libtool autotools-dev autoconf pkg-config libssl-dev
```

```text
sudo apt-get install libboost-all-dev git npm nodejs nodejs-legacy libminiupnpc-dev redis-server
```

```text
add-apt-repository ppa:bitcoin/bitcoin
```

```text
sudo apt-get update
```

```text
apt-get install libdb4.8-dev libdb4.8++-dev
```

```text
curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh -o install_nvm.sh
```

```text
bash install_nvm.sh
```

* After npm is installed you will have to log out and then back into your instance and continue installing dependancies.

```text
source ~/.profile
```

```text
nvm install 0.10.48
```

```text
nvm use 0.10.48
```

```text
nvm alias default 0.10.48
```

```text
nvm use default
```

* Install Apache2 for hosting the front end.

```text
sudo apt-get update
```

```text
sudo apt-get install apache2
```

* Adjust firewall to allow Apache full.

```text
sudo ufw allow 'Apache Full'
```

## Install Qwertycoin

```text
git clone --recurse-submodules https://github.com/qwertycoin-org/qwertycoin
```

```text
cd ./qwertycoin
```

```text
mkdir ./build
```

```text
cd ./build
```

```text
cmake ..
```

```text
cmake --build . --config Release
```

### Start Daemon and Let It Sync

```text
 cd build/src
```

```text
tmux
```

```text
./qwertycoind
```

* Let the blockchain sync before continuing
* To sync the blockchain faster follow [this guide](https://docs.qwertycoin.org/guides/mining/guides/daemon/Load-Checkpoints)
* control b + d to exit tmux

### Start Simple Wallet and Follow Steps to Generate a New Wallet Address

* After you generated a new wallet exit it and run this:

```text
tmux
```

```text
./simplewallet --wallet-file <wallet_name> --password <wallet_password> --rpc-bind-port 8198
```

* control b + d to exit tmux

## Install Pool Software

### Install Dependancies

```text
sudo apt-get install libssl-dev libboost-all-dev
```

```text
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash
```

```text
sudo apt-get install -y nodejs
```

```text
sudo add-apt-repository ppa:chris-lea/redis-server
```

```text
sudo apt-get update
```

```text
sudo apt-get install redis-server
```

* Clone repository

```text
git clone https://github.com/dvandal/cryptonote-nodejs-pool.git pool
```

```text
cd pool && npm update
```

### Pool Configuration

* Copy the `config_examples/qwertycoin.json` file to `config.json`

```text
cp config_examples/qwertycoin.json config.json
```

Change the following variables: Line 2 - Pool host to your pools IP Address Line 30 - Your simplewallet address that you generated Line 138 - Set your API password Line 125-127 - \(Optional\) change pool fees

### Copy website\_example Files to html directory

```text
sudo cp -rf js/ lang/ pages/ themes/ admin.html config.js index.html /var/www/html
```

### Configuring website\_example

* Edit `config.js` to use your pool's specific configuration

### Start the Mining Pool

```text
cd && cd pool
```

```text
node init.js
```

* Your pool should now be visible at your server's IP address
* You can visit your admin page by appending `admin.html` to your server IP address in your browsers search bar like so:

`http://server-ip-address/admin.html`

* Your admin password is your API password you set earlier in `config.json`

