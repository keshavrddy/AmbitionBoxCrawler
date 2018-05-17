#!/usr/bin/env bash

tor --RunAsDaemon 1 --CookieAuthentication 0 --HashedControlPassword "" --ControlPort 8118 --PidFile tor.pid --SocksPort 9050 --DataDirectory tordata/tor

