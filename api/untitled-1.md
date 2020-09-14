# Daemon HTTP RPC Commands

To start Daemon HTTP RPC API server you should specify a port on which server binds \(additionally to standard daemon's arguments\). You can choose any free port. To do that execute the following command from the command line:

`./Qwertycoind --rpc-bind-port=8197`

If you want Daemon to be accessed from other computer not only yours you should also use a `--rpc-bind-ip 0.0.0.0` command. To do that execute the following command from the command line:

`./Qwertycoind --rpc-bind-ip=0.0.0.0 --rpc-bind-port=8197`

## Inputing commands

You can input the commands into any browser but Firefox will give you the best interface for viewing. To begin type in the IP address or domain name of your daemon followed by the rpc port and one of the commands below.

[http://ip\_address:rpc\_port/command](http://ip_address:rpc_port/command)

For example:

[https://pool.qwertycoin.org:8197/getheight](https://pool.qwertycoin.org:8197/getheight)

* The url above will display the current blockchain height.

## Commands

### `getinfo` - returns information related to the network and daemon connection

* Expected output

  ```text
  {
    "already_generated_coins": "129095443585.49424584",
    "alt_blocks_count": 72,
    "block_major_version": 5,
    "block_minor_version": 0,
    "contact": "dev@qwertycoin.org",
    "difficulty": 15525517770,
    "fee_address": "QWC1RALGaP5U8BLJskYR2YVSjr3DQEEuS5xghbtX2mm134YVXgS4RJHZGkeBvXf4BRFLWkv4zHGJ267S9pjwvVt63xwkdYPCwF",
    "grey_peerlist_size": 785,
    "height": 631979,
    "incoming_connections_count": 196,
    "last_block_difficulty": 15501045527,
    "last_block_reward": 10562690450574,
    "last_block_timestamp": 1595189310,
    "last_known_block_index": 631978,
    "min_tx_fee": 100000000,
    "outgoing_connections_count": 7,
    "readable_tx_fee": "1.00000000",
    "rpc_connections_count": 19,
    "start_time": 1591793327,
    "status": "OK",
    "top_block_hash": "ebb71cd6dbbaa2c8079b05ee897b13f22eb48db4b80c0701dddd8f3b1eb2ae95",
    "tx_count": 1763574,
    "tx_pool_size": 0,
    "version": "5.3.1.4068 (f693d25)",
    "white_peerlist_size": 90
  }
  ```

### `getheight` - returns the height of the daemon and the network

* Expected output

```text
{
    "height": 631980,
    "status": "OK"
}
```

### `gettransactions` - returns list of missed transactions

* Expected output

```text
{
    "missed_tx": [],
    "status": "OK",
    "txs_as_hex": []
}
```

### `feeaddress` - returns the address to where the nodes fees are sent

* Expected output

```text
{
    "fee_address": "QWC1RALGaP5U8BLJskYR2YVSjr3DQEEuS5xghbtX2mm134YVXgS4RJHZGkeBvXf4BRFLWkv4zHGJ267S9pjwvVt63xwkdYPCwF",
    "status": "OK"
}
```

### `getpeers` - returns the list of peers connected to the daemon

* Expected output

```text
{
    "peers": [
        "94.130.187.117:8196",
        "195.201.27.148:8196",
        "148.251.115.233:8196",
        "173.212.197.11:8196",
        ...
        "173.249.35.250:8196"
    ],
    "status": "OK"
}
```

### `paymentid` - returns the paymentid of the node

* Expected output

```text
{
    "payment_id": "d4d9671bf684c73209d0f756a81ced9493650d16cb332ea477cc3bdf90522db7"
}
```

