# briefly on files

# 0.
# binary files are manipulated through byte objects
f = open('workfile', 'wb+')
f.write(b'0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2)  # Go to the 3rd byte before the end
f.read(1)
f.close()

# 1.
# using 'with' for automatic file closing
with open('workfile', 'r') as f:
    print(str(f.read()))

# verify that file object is closed
print('File is closed?', repr(f.closed))

# 2.
# serializing to and desearializing from JSON
import json
with open('json.txt', 'w') as outfile:
    # mind the order of the arguments of dump ;)
    json.dump([1, 'simple', 'list'], outfile)

with open('json.txt', 'r') as infile:
    print(json.load(infile))

# NOTE: JSON format matches Python dicts and lists
with open('sample.json', 'r') as infile:
    print(json.load(infile))
