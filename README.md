# Python Star Pattern Assignment

Two star-pattern programs (medium to hard level) written in Python using nested loops and conditionals. Both work for any valid value of `n`; nothing is hard-coded.

## Files

| File | Description |
|------|-------------|
| `hollow_diamond.py` | Hollow diamond for an odd number `n` |
| `butterfly_pattern.py` | Butterfly pattern for `n` rows |

## How to run

```bash
python hollow_diamond.py
python butterfly_pattern.py
```

---

## Question 1: Hollow Diamond

**Approach:** For each row, compute its distance (`offset`) from the nearest tip of the diamond.
- Leading spaces = `middle - offset`
- Spaces between the two stars = `2 * offset - 1`
- The tip rows (`offset == 0`) print only one star.

**Test 1: n = 7**
```
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```

**Test 2: n = 5**
```
  *
 * *
*   *
 * *
  *
```

---

## Question 2: Butterfly Pattern

**Approach:** Split the pattern into an increasing and a decreasing section. For row `r`:
- Stars on each side = `r`
- Spaces in the middle = `2 * (n - r)`

The increasing section runs from row 1 to `n`, and the decreasing section from row `n - 1` back to 1.

**Test 1: n = 5**
```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

**Test 2: n = 3**
```
*    *
**  **
******
**  **
*    *
```
