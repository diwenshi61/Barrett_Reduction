# Modular Reduction

A python script that generates VHDL files describing steps for a modular reduction in hardware.

## Usage

A modular reduction is described by the equation

c = a mod b

where a and b are positive integers.

Two inputs are required to generate the Barrett reduction code:

- The maximum bit width of a

- The value of b

This script creates three VHDL files containing three steps to perform a Barrett reduction in order:

1) Multiplication by a decimal value and flooring

2) Multiplication by an integer value

3) Subtraction and reducing

See "Barrett_reduction_in_hardware.txt" for a complete explanation of these steps.

These hardware components are mostly bare bones and are not connected by a top level component and no testbenches are generated.

Depending on the size of the multiplies, it would make sense to separate the multiplication steps into multiple cycles,
and add more in/outs to the components as necessary, such as a reset, a start signal, a done signal.

Large multiplies are generally slow and not suited to be done in a single clock cycle, which the generated VHDL describes.

## Sample

An example of the generated files is included. The files describe the steps above:

1) multiplier_by_100010001000001111.vhd <==> Multiplication by a decimal value and flooring

2) multiplier_17bits_by_7681.vhd <==> Multiplication by an integer value

3) subtract_from_a_and_reduce.vhd <==> Subtraction and reducing

Recall the modular reduction equation

c = a mod b

These files are generated for a bit width of 30 bits for a and the value of 7681 for b.

The ports should be connected as follows, where the left side denotes the required inputs and the right side the outputs:

1) refers to multiplier_by_100010001000001111.vhd

2) refers to multiplier_17bits_by_7681.vhd

3) refers to subtract_from_a_and_reduce.vhd

-----------------------------------------------------
a                    |            1) a
-----------------------------------------------------
1) a_inv_b           |            2) a_inv_b_floor
-----------------------------------------------------
2) b_a_inv_b_floor   |            3) b_a_inv_b_floor
a                    |            3) a
-----------------------------------------------------
3) c                 |            c
-----------------------------------------------------

Note that the initial value a needs to be reused going into the third step.

## Compatibility

Written for Python 2.7. Modifications needed to use with Python 3 (e.g. replacing raw_input).

Works with VHDL-1993 - does not require 2008.
