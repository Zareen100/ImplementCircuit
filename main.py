# Function for AND gate
def AND_gate(a, b):
    return a & b

# Function for OR gate
def OR_gate(a, b):
    return a | b

# Function for XOR gate
def XOR_gate(a, b):
    return a ^ b

# Function for NOT gate (bitwise NOT)
def NOT_gate(a):
    # In Python, ~a gives the bitwise negation of a.
    # For a single-bit NOT, we use 1 - a since a can only be 0 or 1.
    return 1 - a

# Function to simulate a circuit
# Example: (A AND B) OR (C XOR NOT D)
def simulate_circuit(a, b, c, d):
    # Step 1: A AND B
    and_result = AND_gate(a, b)
    
    # Step 2: NOT D
    not_d = NOT_gate(d)
    
    # Step 3: C XOR NOT D
    xor_result = XOR_gate(c, not_d)
    
    # Step 4: (A AND B) OR (C XOR NOT D)
    final_result = OR_gate(and_result, xor_result)
    
    return final_result

# Example inputs (0 or 1 for binary values)
a = 1  # Input A
b = 0  # Input B
c = 1  # Input C
d = 0  # Input D

# Simulating the circuit with the given inputs
result = simulate_circuit(a, b, c, d)
print(f"Circuit output: {result}")
