#!/bin/bash

NAME="$1"

docker run --rm -v "$PWD:/src" -w /src alpine:latest sh -c "apk add --no-cache musl-dev tcc-libs tcc-libs-static tcc && tcc $NAME -o $NAME.exe && ./$NAME.exe"

# homage to Tiny C Compiler https://www.bellard.org/tcc/ , of course you could just use https://hub.docker.com/_/gcc/
# https://pkgs.alpinelinux.org/package/edge/community/x86/tcc

