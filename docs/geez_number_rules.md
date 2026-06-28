# Geez Number Rules

## Purpose

This document describes the structure and rules of the Geez (Ethiopic) numeral system used in this project. Understanding these rules is essential before implementing the conversion algorithms.

---

# 1. Basic Numeral Symbols

## Ones (1–9)

| Arabic | Geez |
|--------:|:----:|
| 1 | ፩ |
| 2 | ፪ |
| 3 | ፫ |
| 4 | ፬ |
| 5 | ፭ |
| 6 | ፮ |
| 7 | ፯ |
| 8 | ፰ |
| 9 | ፱ |

---

## Tens (10–90)

| Arabic | Geez |
|--------:|:----:|
| 10 | ፲ |
| 20 | ፳ |
| 30 | ፴ |
| 40 | ፵ |
| 50 | ፶ |
| 60 | ፷ |
| 70 | ፸ |
| 80 | ፹ |
| 90 | ፺ |

---

# 2. Special Symbols

| Arabic | Geez |
|--------:|:----:|
| 100 | ፻ |
| 10,000 | ፼ |

These symbols act as multipliers when constructing larger numbers.

---

# 3. Number Construction Rules

## Rule 1: Tens are written before Ones

Example:

20 + 5

```
25 → ፳፭
```

40 + 8

```
48 → ፵፰
```

---

## Rule 2: Hundreds

A number greater than one hundred is formed by placing the multiplier before the hundred symbol.

Examples:

```
100 → ፻

200 → ፪፻

300 → ፫፻

900 → ፱፻
```

Notice that the digit **1** is omitted.

Correct:

```
100 → ፻
```

Incorrect:

```
100 → ፩፻
```

---

## Rule 3: Hundreds with Tens and Ones

Examples:

```
125

↓

100 + 20 + 5

↓

፻፳፭
```

```
347

↓

300 + 40 + 7

↓

፫፻፵፯
```

---

## Rule 4: Ten-Thousands

The symbol **፼** represents 10,000.

Examples:

```
10,000 → ፼

20,000 → ፪፼

30,000 → ፫፼
```

Again, the leading **1** is omitted.

Correct:

```
10,000 → ፼
```

Incorrect:

```
10,000 → ፩፼
```

---

# 5. Pattern Observations

The Geez numeral system is built using reusable symbols rather than assigning a unique symbol to every number.

Most numbers can be represented as combinations of:

- Ones
- Tens
- Hundreds
- Ten-thousands

Examples:

```
274

↓

200 + 70 + 4

↓

፪፻፸፬
```

```
586

↓

500 + 80 + 6

↓

፭፻፹፮
```

---

# 6. Algorithm Design Observations

The following observations guided the implementation of this project:

- Numbers from 1–9 have unique symbols.
- Multiples of ten have unique symbols.
- Dictionaries provide fast symbol lookup.
- Arabic → Geez conversion is performed by decomposing the number into place values and converting each part.
- Geez → Arabic conversion is performed by reading symbols from left to right and applying multiplication when encountering **፻** or **፼**.

---

# 7. Limitations

This implementation:

- Supports positive integers only.
- Supports values up to millions.
- Assumes the input follows valid Geez numeral rules.
- Does not process invalid or malformed Geez numerals.
