// using recursion call

function factorial(num) {

  if (num === 0) {
    return 1;
  }

  return num*factorial(num-1)
}

console.log(factorial(4))

// using iteratively

function factorial_i(num) {
  var i;
  let answer = 1
    for (i = 1; i <= num; i++) {
      answer = answer*i
    } 
  return answer
}

console.log(factorial_i(4))