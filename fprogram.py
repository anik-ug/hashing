import hashlib
def read_dictionary(file_path):
   with open(file_path,'r') as file:
      return [line.strip() for line in file]

def crack_password(target_hash, dictionary):
   for i in dictionary:
      if hashlib.sha256(i.encode()).hexdigest() == target_hash:
         return i
   else:
       return None


if __name__=='__main__':
   x=input("paste the hash here: ")
   target_hash = x
   
   file_path = r'/Users/anikkumar/Desktop/development/python/hashing/Dictionary.txt'

   dictionary =read_dictionary(file_path)
   cracked_password=crack_password(target_hash,dictionary)
   if cracked_password:
      print("password found",cracked_password)
   else:
      print("password not found")