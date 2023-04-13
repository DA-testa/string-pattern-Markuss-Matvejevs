def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    if input().strip() == "F":
      with open("tests/06") as file:
        return (file.readline().strip(), file.readline().strip())
    
    # if we're not reading from a file, read from standard input
    return (input().strip(), input().strip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

# algorithm: https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm#Hash_function_used
def hash(string, rolling_total = None):
    if not string:
      return rolling_total

    if rolling_total == None:
      return hash(string[1:], ord(string[0]))

    return hash(string[1:], ((rolling_total * 256) % 101 + ord(string[0])) % 101)

def rehash(old_letter, old_hash, new_letter, hash_len):
    return [ ( 4   + 101         -  97 * [(256%101)*256] % 101 ) * 256         +    97 ] % 101

def get_occurrences(pattern, text):
    pattern_hash = hash(pattern)
    slice_hash = None
    occurrences = []
    pattern_len = len(pattern)
    print(pattern_hash)
    for i in range(len(text) - pattern_len + 1):
      text_slice = text[i:i + pattern_len]

      # calculate the new hash by adding only the character that was added to the slice
      slice_hash = rehash(text_slice)
      print(i, slice_hash)
      # only compare strings if the hashes match
      if pattern_hash == slice_hash and text_slice == pattern:
        occurrences.append(i)

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))