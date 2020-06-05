# XMR-Stak Linux

Native binaries may be available for your distribution's package manager.

If no binaries are available, or you prefer to compile, follow these instructions:

## Ubuntu 16.04

If you want to use your GPU for mining, do the following:

### For nVidia GPU’s

* Install drivers for your card
* Download the latest CUDA Toolkit from [here](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64).
* Download the base installer and follow the compilation instructions
* Download every patch one-by-one in order and apply the patches
* After that, you should be good.

### For AMD GPU’s

* Install drivers for your card
* download the latest APP SDK from [here](https://developer.amd.com/amd-accelerated-parallel-processing-app-sdk/). It should have the name `AMD-APP-SDKInstaller-v(version number)-GA-linux64.tar.bz2`
* Extract it
* Open the terminal wherever it is located
* \(optional\) name it to something simpler
* In the terminal, type `./(name).sh`
* After installing, you should be good.

### Running with CPU, AMD & nVidia GPUs

1. Open the terminal and install dependencies by running this command

`sudo apt install libmicrohttpd-dev libssl-dev cmake build-essential libhwloc-dev`

1. Clone the package

`git clone https://github.com/fireice-uk/xmr-stak.git`

1. Make a directory

`mkdir xmr-stak/build`

1. Move over there

`cd xmr-stak/build`

1. Run cmake

`cmake ..`

* If you don’t have nVidia GPUs, type:

`cmake .. -DCUDA_ENABLE=OFF`

* If you don’t have AMD GPUs, type

`cmake .. -DOpenCL_ENABLE=OFF`

* If you have neither \(only CPU mining\) type

`cmake .. -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF`

1. Finish building it

`make install`

1. XMR-Stak will now be located in `/home/user/xmr-stak/build/bin`
2. Type the following to begin configuration

`./xmr-stak`

1. Check [XMR-Stak Setup and Configuration](xmr-stak.md#XMR-Stak-Setup-and-Configuration) to learn how to configure the miner.

