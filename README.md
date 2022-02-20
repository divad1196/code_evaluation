# Code Evaluation

The goal is to provide a safer way to eval/exec code and provide some utilities.

DISCLAIMER: This is still not sandboxed nor fool-proof and will never be.
The user should not trust unverified inputs and is the only one responsible for the extra variables he provides.
Even though the modules allow to change the globals variables used for eval/exac, I am not responsible for any addons to the globals either.



## Usage

### Basique eval_code/exec_code

Work in the same way as eval/exec, but with limited set of action possibles. Especially:

* IO is removed (no open/file/print/... available)
* No complex declaration (classes, functions, ...)
* we are limited to a single statement