#!/usr/bin/env ruby

input_string = ARGV[0]

matches = input_string.scan(/^\d{10}$/)

puts matches.join
