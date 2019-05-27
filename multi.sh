#!/bin/sh
number=$1

default="Not Found!"
goval=$default
groovyval=$default
nodeval=$default
pythonval=$default
rubyval=$default
swiftval=$default

fname="Euler$number"

gofile="Go/$fname.go"
golibs="Go/sieve.go"

groovyfile="Groovy/$fname.groovy"

nodefile="Node/$fname.js"
pythonfile="Python/$fname.py"
rubyfile="Ruby/$fname.rb"

csdir="CSharp/$fname"

chmod +x "$groovyfile" "$pythonfile" "$rubyfile" "$nodefile"> /dev/null 2>/dev/null

if [ -f "$gofile" ]; then goval=$(go run "$gofile" $golibs 2>/dev/null); fi
if [ -f "$groovyfile" ]; then groovyval=$($groovyfile 2>/dev/null); fi
if [ -f "$nodefile" ]; then nodeval=$($nodefile 2>/dev/null); fi
if [ -f "$pythonfile" ]; then pythonval=$($pythonfile 2>/dev/null); fi
if [ -f "$rubyfile" ]; then rubyval=$($rubyfile 2>/dev/null); fi
if [ -d "$csdir" ]; then csval=$(dotnet run --project "$csdir"); fi

echo "
Go:         $goval
Groovy:     $groovyval
Node.js:    $nodeval
Python:     $pythonval
Ruby:       $rubyval
CSharp:     $csval"
