package main

import (
  "fmt"
  //"github.com/drio/drio.go/math"
)

// Problem 23
//
//    02 August 2002
//
//    A perfect number is a number for which the sum of its proper divisors
//    is exactly equal to the number. For example, the sum of the proper
//    divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is
//    a perfect number.
//
//    A number n is called deficient if the sum of its proper divisors is
//    less than n and it is called abundant if this sum exceeds n.
//
//    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
//    smallest number that can be written as the sum of two abundant numbers
//    is 24. By mathematical analysis, it can be shown that all integers
//    greater than 28123 can be written as the sum of two abundant numbers.
//    However, this upper limit cannot be reduced any further by analysis
//    even though it is known that the greatest number that cannot be
//    expressed as the sum of two abundant numbers is less than this limit.
//
//    Find the sum of all the positive integers which cannot be written as
//    the sum of two abundant numbers.
const limit = 28123

type abundants map[int]bool

func main() {
  mAbunt := findAbundants(limit)
  sum := 0
  for n := 1; n <= limit; n++ {
    if !canBeWrittenAsAbundants(n, mAbunt) {
      sum += n
    }
  }
  fmt.Println(sum)
}

func canBeWrittenAsAbundants(n int, mAbunt abundants) bool {
  for a, _ := range mAbunt {
    if mAbunt[n-a] {
      return true
    }
  }
  return false
}

func findAbundants(lim int) abundants {
  mAbu := make(abundants)
  for i := 1; i <= limit; i++ {
    sumDivs := findProperDivisors(i)
    if sumDivs > i {
      mAbu[i] = true
    }
  }
  return mAbu
}

func findProperDivisors(n int) int {
  sumDivs := 0
  for i := 1; i < n; i++ {
    if n%i == 0 {
      sumDivs += i
    }
  }
  return sumDivs
}
