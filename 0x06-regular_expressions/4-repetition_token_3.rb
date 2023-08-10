#!/usr/bin/env ruby

input_string = ARGV[0]

matches = input_string.scan(/hbt*n/)

puts matches.join
