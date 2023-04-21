#!/usr/bin/node

// a function that returns the reversed version of a list

exports.esrever = function (list) {
  const newList = [];
  for (let position = list.length - 1; position >= 0; position--) {
    newList.push(list[position]);
  }
  return newList;
};
