# Hosting Web Wallet

![](../.gitbook/assets/image%20%283%29.png)

The Qwertycoin web wallet does everything client-side to give the best privacy to users. The API servers are currently only used to optimize the communication with the daemon and compress the blockchain.

## Install prerequisites

* You will need to install node.js and NPM \(node's package manager\) to compile the web wallet. For Linux \(Ubuntu\) enter the code below:

```text
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
```

## Compilation

* Clone the repository:

```text
git clone https://github.com/qwertycoin-org/webwallet-js.git
```

* Enter `webwallet-js` and run the following commands:

```text
npm install
nodejs ./node_modules/typescript/bin/tsc --project tsconfig.json
nodejs build.js
```

The first line installs the required dependancies \(typescript\) and the second compiles the typescript code.

## Deployment

You can host the web wallet using Apache or Nginx. For this tutorial I will be using Apache.

* Install Apache

```text
sudo apt-get update

sudo apt-get install apache2

sudo ufw allow 'Apache Full'
```

* Copy everything in the `src` directory to the html directory.

```text
sudo cp -rf api.html config.ts lib/ service-worker-raw.js api.js d/ manifest.json service-worker-raw.ts api.ts index.html model/ translations/ assets/ index.js pages/ utils/ config.js index.ts providers/ workers/ /var/www/html
```

## Edit configuration

You will have to edit the file `src/config.ts` in order to change the API endpoint \(point it to your daemon\). Once that is complete you should now see the web wallet at your address like so:

