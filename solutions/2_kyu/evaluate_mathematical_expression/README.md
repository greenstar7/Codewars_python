# [2 Kyu: Evaluate mathematical expression][1]

## Backus-Naur form

``` BNF
expr : term ((plus | minus) term)*

term : factor ((mul | div) factor)*

factor : plus  factor
       | minus factor
       | number
       | lpar expr rpar

```

[1]: https://www.codewars.com/kata/evaluate-mathematical-expression/train/python
