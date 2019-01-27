#!/bin/sh
number=$1

default="Not Found!"
cval=$default
goval=$default
groovyval=$default
nodeval=$default
pwshval=$default
pythonval=$default
rubyval=$default
swiftval=$default

fname="Euler$number"

cfile="C/$fname.c"
gofile="Go/$fname.go"
groovyfile="Groovy/$fname.groovy"
nodefile="Node/$fname.js"
pwshfile="Powershell/$fname.ps1"
pythonfile="Python/$fname.py"
rubyfile="Ruby/$fname.rb"
swiftfile="Swift/$fname.swift"

chmod +x "$groovyfile" "$pythonfile" "$rubyfile" "$swiftfile" "$pwshfile" "$nodefile"> /dev/null 2>/dev/null

if [ -f "$cfile" ]; then gcc $cfile -o C/$fname.o; cval=$(C/$fname.o); fi
if [ -f "$gofile" ]; then goval=$(go run "$gofile" 2>/dev/null); fi
if [ -f "$groovyfile" ]; then groovyval=$($groovyfile 2>/dev/null); fi
if [ -f "$nodefile" ]; then nodeval=$($nodefile 2>/dev/null); fi
if [ -f "$pwshfile" ]; then pwshval=$($pwshfile 2>/dev/null); fi
if [ -f "$pythonfile" ]; then pythonval=$($pythonfile 2>/dev/null); fi
if [ -f "$rubyfile" ]; then rubyval=$($rubyfile 2>/dev/null); fi
if [ -f "$swiftfile" ]; then swiftval=$($swiftfile 2>/dev/null); fi

echo "
C:          $cval
Go:         $goval
Groovy:     $groovyval
Node.js:    $nodeval
Powershell: $pwshval
Python:     $pythonval
Ruby:       $rubyval
Swift:      $swiftval"
