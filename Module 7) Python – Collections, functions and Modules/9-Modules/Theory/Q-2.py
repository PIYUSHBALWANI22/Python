"""
Standard library modules: math, random. 

--> In Python's standard library, the `math` and `random` modules are essential tools that provide mathematical operations and random number generation, respectively.


 1. `math` Module
The `math` module offers functions for mathematical calculations beyond the basic operations like addition or subtraction. Key features include:

- Trigonometric Functions: Calculate sine, cosine, tangent, etc. (e.g., `math.sin(x)`, `math.cos(x)`).
- Logarithmic and Exponential Functions: Perform operations like natural logarithms and exponentiation (e.g., `math.log(x)`, `math.exp(x)`).
- Constants: Access mathematical constants such as:
  - `math.pi` (≈ 3.14159)
  - `math.e` (≈ 2.71828)
- Other Operations:
  - Rounding up or down: `math.ceil(x)`, `math.floor(x)`
  - Square root: `math.sqrt(x)`
  - Factorials: `math.factorial(x)`
  - Greatest common divisor: `math.gcd(a, b)`


 2. `random` Module
The `random` module is designed for generating random numbers and performing randomization-related tasks. It is widely used in simulations, games, and testing. Key features include:

- Random Numbers:
  - `random.random()`: Generates a random float between 0.0 and 1.0.
  - `random.randint(a, b)`: Returns a random integer between `a` and `b`, inclusive.
  - `random.uniform(a, b)`: Generates a random float between `a` and `b`.
- Shuffling and Sampling:
  - `random.shuffle(seq)`: Randomly shuffles a sequence (like a list).
  - `random.sample(population, k)`: Chooses `k` random unique elements from the population.
- Choosing Random Elements:
  - `random.choice(seq)`: Picks a random element from a sequence.
- Seeding:
  - `random.seed(x)`: Initializes the random number generator for reproducibility.


Both modules are fundamental and can handle a wide range of mathematical or randomization tasks in Python.
"""