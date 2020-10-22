function reverse_(str_input) {
  reverse_str = ""
  for (i in str_input) {
    reverse_str += str_input[str_input.length-1-i]
  }
  return reverse_str
}

// Check the code now
console.log(reverse("I am Shantanu"))

function reverse(str_input) {
  
  if (!str_input || str_input.length < 2 || typeof str_input !== 'string') {
    return "bad input!"
  } 

  reverse_str = ""
  for (i in str_input) {
    reverse_str += str_input[str_input.length-1-i]
  }
  return reverse_str

}