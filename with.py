# try:
#     stream = open('output.txt','wt')
#     stream.write('Lorem Ipsum Dollar')
# finally:
#     stream.close()

with open('output.txt','wt') as stream:
    stream.write('Lorem Ipsum Dollar')