package main

import "fmt"

// Problem 24
//
//    16 August 2002
//
//    A permutation is an ordered arrangement of objects. For example, 3124
//    is one possible permutation of the digits 1, 2, 3 and 4. If all of the
//    permutations are listed numerically or alphabetically, we call it
//    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
//
//    012   021   102   120   201   210
//
//    What is the millionth lexicographic permutation of the digits 0, 1, 2,
//    3, 4, 5, 6, 7, 8 and 9?
//
//
// Solution based on: http://en.wikipedia.org/wiki/Factorial_number_system
//
//                                  4041000! → (4,0,6,2,1,3,5)
// factoradic:  4          0                        4        1          0          0        0!
//              |          |                        |        |          |          |        |
//     (0,1,2,3,4,5,6) -> (0,1,2,3,5,6) -> (1,2,3,5,6) -> (1,2,3,5) -> (1,3,5) -> (3,5) -> (5)
//              |          |                        |        |          |          |        |
// permutation:(4,         0,                       6,       2,         1,         3,       5)
//
const maxNum = 9
const permNumber = 999999

func main() {
  fmt.Println(findPerm(factoradicOf(permNumber), initSet()))
}

func findPerm(fRadic []int, set []int) []int {
  perm := []int{}
  for i := 0; i < len(fRadic); i++ {
    index := fRadic[i]
    perm = append(perm, set[index])
    set = append(set[0:index], set[index+1:len(set)]...)
  }
  return perm
}

// factoradicOf finds the factoradic representation of num
func factoradicOf(permNum int) []int {
  maxDiv := 0
  for i := 12; i > 0; i-- {
    if factorial(i)-1 < permNum {
      maxDiv = i
      break
    }
  }

  fRadic := []int{}
  a := permNum // a/b = c (r)
  for b := maxDiv; b >= 0; b-- {
    fRadic = append(fRadic, a/factorial(b))
    a = a % factorial(b)
  }

  return fRadic
}

func initSet() []int {
  m := make([]int, 10)
  for i := 0; i <= maxNum; i++ {
    m[i] = i
  }
  return m
}

func factorial(n int) int {
  if n == 1 || n == 0 {
    return 1
  }
  return n * factorial(n-1)
}
