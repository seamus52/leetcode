#!/usr/bin/env bash

solve() {
    CNT=$(wc -w $1)
    if [[ -n $1 && $CNT -ge 500 && $CNT -le 1000 ]]; then
        echo "Good Job!"
    else
        echo "Revise the essay"
    fi
}
