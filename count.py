# Initialize variables
file = "README.md"
amnt = 0

# Loop through all lines
with open(file, 'r') as f:
  for line in f:
    amnt += 1

# Create html file
out = open('out.html', 'wb')

message = """
<html>
  <head></head>
  <body><p>Number of lines in README.md is """ + str(amnt) + """</p></body>
</html>
          """

out.write(message)
out.close()

print "Created out.html"
