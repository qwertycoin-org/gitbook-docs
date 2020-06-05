# Cloud Mining

## Setting up EC2 instance

### Create AWS Account

* Create an account with [Amazon AWS](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start).

### Setup an Instance

* On the home page, click the services tab and then go to compute and click 'EC2'. Once you are there you will chose your region on the top of the page in the header section. Next click the 'Launch Instance' button at the center of the page and then select an AMI. For this tutorial I am using Ubuntu Server 16.04 LTS.
* Next you will need to choose an instance type. I am just going to use the preselected t2.micro for the tutorial. For the purpose of mining, the Compute Optimized and the GPU instances are your best choices.
* You can then skip to step six and under the source tap select my IP.
* Next press Review and Launch and then create a new key pair to be able to connect with your instance. Once the instance is live, you can connect to your instance using an SSH through Terminal, PuTTY or similar program.
* The final step is to install your mining software of choice and start mining! With a compute optimized c4.8xlarge instance you will get about 750 H/s when mining for Cryptonote currencies such as Qwertycoin.

### SSH into the Isnstance

1. Download key pair that you created earlier
2. Make sure you are in the same directory as the key and allow permissions

`chmod 600 <key-name>.pem`

1. SSH into instance

`ssh -i <key-name>.pem ubuntu@<EC2-IP-Address>`

## Install Mining Software

1. In the terminal install dependencies by running this command

`sudo apt install libmicrohttpd-dev libssl-dev cmake build-essential libhwloc-dev git`

1. Clone the package

`git clone https://github.com/fireice-uk/xmr-stak.git`

1. To remove donations, type

`nano xmr-stak/xmrstak/donate-level.hpp`

Change `constexpr double fDevDonationLevel = 2.0 / 100.0;`

to `constexpr double fDevDonationLevel = 0.0 / 100.0;`

1. Make build directory

`mkdir xmr-stak/build`

1. Move into the new directory

`cd xmr-stak/build`

1. Run cmake

`cmake .. -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF`

1. Finish building it

`make install`

1. XMR-Stak will now be located in `/home/user/xmr-stak/build/bin`
2. Move to where it's at

`cd bin`

1. Launch XMR-Stak

`./xmr-stak`

1. Check [XMR-Stak Setup and Configuration](https://docs.qwertycoin.org/guides/mining/guides/mining/XMR-Stak)

