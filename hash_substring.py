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

# computing the hash of the next substring:
# https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm#Hash_function_used
def rehash(old_letter, old_hash, new_letter, pattern_len):
    base_value = 256

    # raise 256 to the power of pattern_len - 1 and modulo 101 each value to avoid overflow
    for i in range(pattern_len - 2):
      base_value = (base_value % 101) * 256
    
    base_value %= 101
    
    return ((old_hash + 101 - ord(old_letter) * base_value) * 256 + ord(new_letter)) % 101

def get_occurrences(pattern, text):
    pattern_hash = hash(pattern)
    slice_hash = None
    text_slice = ""
    pattern_len = len(pattern)

    occurrences = []
    
    for i in range(len(text) - pattern_len + 1):
      new_slice = text[i:i + pattern_len]

      if not slice_hash:
        # we need to generate a hash for the slice when we are at the beginning of the input text
        slice_hash = hash(new_slice)
      else:
        # calculate the new hash by adding only the character that was added to the slice
        slice_hash = rehash(text_slice[0], slice_hash, new_slice[-1], pattern_len)
        
      text_slice = new_slice

      # only compare strings if the hashes match
      if pattern_hash == slice_hash and text_slice == pattern:
        occurrences.append(i)

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))