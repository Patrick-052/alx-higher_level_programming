#!/usr/bin/node

exports.converter = function (base) {
  return function baseChange (num) {
    return num.toString(base);
  };
};
