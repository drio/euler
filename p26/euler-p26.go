package main

import (
  "fmt"
  drdmath "github.com/drio/drio.go/math"
  "math/big"
  "os"
  "time"
)

// Problem 26
//
//    13 September 2002
//
//    A unit fraction contains 1 in the numerator. The decimal representation
//    of the unit fractions with denominators 2 to 10 are given:
//
//      ^1/[2]  =  0.5
//      ^1/[3]  =  0.(3)
//      ^1/[4]  =  0.25
//      ^1/[5]  =  0.2
//      ^1/[6]  =  0.1(6)
//      ^1/[7]  =  0.(142857)
//      ^1/[8]  =  0.125
//      ^1/[9]  =  0.(1)
//      ^1/[10] =  0.1
//
//    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
//    can be seen that ^1/[7] has a 6-digit recurring cycle.
//
//    Find the value of d < 1000 for which ^1/[d] contains the longest
//    recurring cycle in its decimal fraction part.
//
// References:
// http://mathforum.org/library/drmath/view/69422.html
// http://en.wikipedia.org/wiki/Repeating_decimal
func main() {
  start := time.Now()
  max, num := 0, 0
  for i := 1; i < 1000; i++ {
    if drdmath.IsPrime(uint64(i)) {
      if r := rcl(i); r > max {
        max, num = r, i
      }
    }
  }
  fmt.Printf("the recurring cycle of 1/%d is %d.\n", num, max)
  end := time.Now()
  fmt.Fprintln(os.Stderr, end.Sub(start))
}

func rcl(n int) int { // recurrent cycle length
  if n%2 == 0 || n%5 == 0 {
    return 0
  }
  i := 1
  for {
    if findBigRem(i, n) == 0 {
      break
    }
    i++
  }
  return i
}

// findBigRem implements this with big numbers: (10^pten - 1) % n
func findBigRem(pten, n int) int {
  bint := big.NewInt(1)
  for i := 0; i < pten; i++ {
    bint = bint.Mul(bint, big.NewInt(10))
  }
  bint = bint.Sub(bint, big.NewInt(1))
  rem := bint.Rem(bint, big.NewInt(int64(n)))
  return int(rem.Int64())
}
