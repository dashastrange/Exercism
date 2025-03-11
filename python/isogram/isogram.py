def is_isogram(string):
   clean_string = string.lower().replace("-","").replace(" ","")

   if len(clean_string) != len(set(clean_string)):
      return False
   else:
      return True