#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from java.lang import ClassLoader
from java.io import InputStreamReader, BufferedReader, OutputStreamWriter, FileOutputStream, File
import java.lang.Byte
import jarray
import subprocess
import os
import array
from org.apache.commons.io import IOUtils

print "We are in python"
fileStream = File("output")

inStream =  ClassLoader.getSystemClassLoader().getResourceAsStream("exec/go/hello")
out = FileOutputStream(fileStream)
IOUtils.copy(inStream, out)
fileStream.setExecutable(True)
out.flush()
out.close()
function_call = subprocess.Popen(["./output"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = function_call.stdout.read()
print output
# print(function_call)
