# kubectl-cli (A shell for kubectl)
Simple python wrapper to make kubectl interactive

## What
kubectl-cli runs in a continuous command loop, simulating an interactive shell. It also displays a prompt (similar to the one you see when you open any sql cli or a bash shell) and shows <code>namespace@current context></code>. This is extremely helpful when you have to manage multiple clusters and you want to make sure you are executing commands against the right cluster. Don't end up executing a command meant for test cluster on a production cluster!

## What it is not
kubectl-cli is not a replacement for kubectl, rather it is a very thin warpper around the kubectl command. The objective is not to wrap kubectl commands, but rather to make running the kubectl command convenient.

## Why
3 primary reasons. One - I did not want to enter the command name (even if it is a single 'k' using alias) every time, Two - I wanted to know which cluster I am executing the command for and Three - I did not want to enter namespace for every command.

## How
Just download and run <code>kubectl-cly.py</code>

If the required dependencies are installed and available, you would be greeted with a prompt with default namespace and the current kubectl context. You can enter any kubectl command without entering 'kubectl' or any alias. E.g. instead of <code>kubectl get pods</code> simply enter <code>get pods</code>

When you are done enter <code>exit</code> or <code>x</code> to exit from the command loop.

kubectl-cli implemented as a very thin python wrapper over kubectl command. Consequently, you will need the 'kubectl' installed, and configured for one or more clusters. Since kubectl-cli wrapper is written in python, you will also need python installed.

## Features
<ul>
<li>Displays prompt with namespce and current context
<li>Get list of configured kubectl contexts using get_contexts
<li>Change context using set_context
<li>Set namespace to be used when executing command
<li>Clear the screen using clear command
</ul>
