# heimdallr
A tool for semantic binary profiling and adaptive fuzzing.

## Goals

### Phase 1
1. Identify control paths, and produce a map of the binary in terms of these control paths.
2. Identify when the control path makes a call to a library/system call, and log it.
### Phase 2
1. Build a table mapping the functioning of each library/system call to its usage.
2. Use this table to build a profile for the program, showing what types of things each control path does.
### Phase 3
1. Use this profile to predict which kind of fuzzer would work best for that control path.
### Phase 4
1. Enable detection of purpose of a block of code directly(probably through ML).

## Techniques
Control paths are identified using control-flow graph analysis(a static analysis technique), which provides us with a list of functions.
Each function is then symbolically executed, and each external call made is matched against a table to determine it's purpose.
This data is then analyzed to produce an overall functioning of the program.

## Profile format
TODO

## Parallelization scheme
TODO
