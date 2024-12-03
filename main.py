def main():
#   read file content
  with open("/home/nerdy/workspace/github.com/nerdymax/BookBot/books/frankeinstein.txt") as f:
    file_contents= f.read()
    print(file_contents)
  print("--- Begin report of books/frankenstein.txt ---")
  convert(file_contents) 
  
  result= count(file_contents)
  
  print(result)
  print("--- End report ---")
# count number of words in the document
def convert(contents):
   words= contents.split()
   print(f' {len(words)} was found in the document') 
  
# number of time each character appeared

def count(content):
  char_count= {}
  for cha in content:
    cha = cha.lower()
    if cha in char_count:
     
     char_count[cha] +=1
     
     
     

     
    else:
      char_count[cha]=1
  for char, value in char_count.items():
      print(f"The '{char}' character was found {value} times")
 
  
main()
  