#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((accumulator, element) => {
    if (element === searchElement) {
      accumulator += 1;
    }
    return accumulator;
  }, 0);
  return count;
};
