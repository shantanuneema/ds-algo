
function merge_sorted_arrays(a, b) {
    
    const merged_array = [];
    let a_item = a[0];
    let b_item = b[0];
    let i = 1;
    let j = 1;

    if (a.length === 0) {
        return b;
    }
    if (b.length === 0) {
        return a
    }
    if (a.length === 0 && b.length === 0) {
        return []
    }

    while (a_item || b_item){
      if (b_item === undefined || a_item < b_item) {
      merged_array.push(a_item);
      a_item = a_item[i];
      i++;
      } else {
      merged_array.push(b_item);
      b_item = b_item[j];
      j++;
      }
    }
  return merged_array
}

a = [2,3,4,4];
b = [0,1,1,8,10,12];

function merge_sorted_arrays_(a, b) {

  var out_array = []
  out_array.length = a.length + b.length

  let i = 0;
  let j = 0;

  while (i + j < out_array.length) {
    if (i < a.length && j < b.length) {
      if (a[i] < b[j]) {
        out_array[i+j] = a[i];
        i++;
      } else {
        out_array[i+j] = b[j];
        j++;
      }
    } else if (i < a.length) {
      out_array[i+j] = a[i];
      i++;
    } else if (j < b.length) {
      out_array[i+j] = b[j];
      j++;
    }
  }
  return out_array
}

console.log(merge_sorted_arrays([0,3,4,31], [3,4,6,30]))
console.log(merge_sorted_arrays_(a, b))
