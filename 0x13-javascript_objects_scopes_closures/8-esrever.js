#!/usr/bin/node
exports.esrever = function (list) {
  let new_Arr = [];
  for (let i = list.length - 1; i >= 0; i--) {
      new_Arr.push(list[i]);
  }
  return(new_Arr);
}
