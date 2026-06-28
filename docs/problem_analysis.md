# Geez-Arabic Number Converter Problem Analysis

## 1. Problem Statement

Develop a system that converts numbers between the Geez numeral system and the Arabic numeral system. The system should support both conversion directions and handle numbers up to millions.

## 2. Problem Understanding

The system accepts a number and the conversion direction selected by the user. If the input is an Arabic number, the system converts it into its Geez equivalent. If the input is a Geez number, the system converts it into its Arabic equivalent.

The system should correctly interpret the symbols and rules of the Geez numeral system while producing an accurate conversion.

## 3. Inputs and Outputs

Input:

- Conversion direction
- Number (Arabic or Geez)

Output:

- Equivalent number in the other numeral system

## 4. Constraints

- Numbers must be within the supported range (up to millions).
- The system must support both Arabic-to-Geez and Geez-to-Arabic conversion.
- Input must represent a valid number.

## 5. Assumptions

- The user selects the conversion direction.
- Arabic numbers are positive integers.
- Geez input contains valid Geez numeral symbols.
- Invalid inputs are outside the scope of this implementation.

## 6. Initial Approach (Dictionary Mapping)

I first analyzed the Geez numeral system and observed that it is built from a limited number of symbols representing ones, tens, hundreds, and ten-thousands.

Instead of using many conditional statements, I decided to store these mappings in dictionaries for fast lookup.

### Algorithm

1. Create dictionaries for ones, tens, and special symbols.
2. Read the conversion direction.
3. Accept the user's input.
4. If the input is Arabic:
   - Break the number into groups.
   - Convert each group using the dictionaries.
   - Combine the Geez symbols.
5. If the input is Geez:
   - Read one symbol at a time.
   - Find its value using the dictionaries.
   - Apply multiplication for special symbols such as ፻ and ፼.
   - Produce the equivalent Arabic number.
6. Display the converted result.

### Observation

Using dictionaries makes symbol lookup simple and efficient while keeping the implementation modular and easy to extend.

## 7. Improved Approach (Modular Design)

### Motivation

As the project grew, separating all logic into one file became difficult to maintain. I therefore separated the program into modules so that each conversion algorithm has a single responsibility.

### Key Observation

The two conversion directions solve different problems.

- Arabic to Geez constructs symbols from numeric values.
- Geez to Arabic interprets symbols and calculates the numeric value.

Separating these algorithms improves readability, testing, and maintenance.

### Module Design

- arabic_to_geez.py
- geez_to_arabic.py
- converter.py (program entry point)

## 8. Complexity Analysis

### Arabic to Geez

Time Complexity: O(d)

Space Complexity: O(1)

where d is the number of digits processed.

### Geez to Arabic

Time Complexity: O(n)

Space Complexity: O(1)

where n is the number of Geez symbols in the input.

Both algorithms process the input only once while maintaining a small number of variables.
