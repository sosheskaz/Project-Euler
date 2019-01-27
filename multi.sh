#!/bin/sh
number=$1

default="Not Found!"
goval=$default
groovyval=$default
pythonval=$default
rubyval=$default
swiftval=$default

fname="Euler$number"

gofile="Go/$fname.go"
groovyfile="Groovy/$fname.groovy"
pythonfile="Python/$fname.py"
rubyfile="Ruby/$fname.rb"
swiftfile="Swift/$fname.swift"

chmod +x "$groovyfile" "$pythonfile" "$rubyfile" "$swiftfile" > /dev/null 2>/dev/null

if [ -f "$gofile" ]; then goval=$(go run "$gofile" 2>/dev/null); fi
if [ -f "$groovyfile" ]; then groovyval=$($groovyfile 2>/dev/null); fi
if [ -f "$pythonfile" ]; then pythonval=$($pythonfile 2>/dev/null); fi
if [ -f "$rubyfile" ]; then rubyval=$($rubyfile 2>/dev/null); fi
if [ -f "$swiftfile" ]; then swiftval=$($swiftfile 2>/dev/null); fi

echo "
Go:     $goval
Groovy: $groovyval
Python: $pythonval
Ruby:   $rubyval
Swift:  $swiftval"
