#!/bin/sh
number=$1

default="Not Found!"
goval=$default
groovyval=$default
nodeval=$default
pythonval=$default
rubyval=$default
swiftval=$default
kotlinval=$default

fname="Euler$number"

gofile="Go/$fname.go"
golibs="Go/sieve.go Go/combinatorics.go"

groovyfile="Groovy/$fname.groovy"

nodefile="Node/$fname.js"
pythonfile="Python/$fname.py"
rubyfile="Ruby/$fname.rb"

csdir="CSharp/$fname"

kotlincdir="Kotlin/bin"
kotlinfile="Kotlin/$fname.kt"
kotlinlibs=Kotlin/Sieve.kt /workspace/Kotlin/Combinatorics.kt
kotlinbin="$kotlincdir/$fname.jar"

chmod +x "$groovyfile" "$pythonfile" "$rubyfile" "$nodefile"> /dev/null 2>/dev/null

if [ -f "$gofile" ]; then goval=$(go run "$gofile" $golibs 2>/dev/null); fi
# if [ -f "$groovyfile" ]; then groovyval=$(groovy $groovyfile 2>/dev/null); fi
if [ -f "$nodefile" ]; then nodeval=$($nodefile 2>/dev/null); fi
if [ -f "$pythonfile" ]; then pythonval=$($pythonfile 2>/dev/null); fi
if [ -f "$rubyfile" ]; then rubyval=$($rubyfile 2>/dev/null); fi
if [ -d "$csdir" ]; then csval=$(dotnet run --project "$csdir"); fi
if [ -f "$kotlinfile" ];
then
    kotlinc "$kotlinfile" $kotlinlibs -include-runtime -d "$kotlinbin" > /dev/null 2>/dev/null \
    && kotlinval=$(java -jar "$kotlinbin" 2> /dev/null)
fi

echo "
CSharp:     $csval
Go:         $goval
Kotlin:     $kotlinval
Node.js:    $nodeval
Python:     $pythonval
Ruby:       $rubyval"
