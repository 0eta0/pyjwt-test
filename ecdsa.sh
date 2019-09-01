#!/bin/bash
openssl ecparam -genkey -name secp256k1 -out key-pair.pem
openssl pkcs8 -topk8 -inform pem -in key-pair.pem -outform pem -nocrypt -out private.pem
openssl ec -in key-pair.pem -pubout -outform pem -out public.pem
rm key-pair.pem
