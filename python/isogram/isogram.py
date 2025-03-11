def is_isogram(string):
   clean_string = string.lower().replace("-","").replace(" ","")

   return len(clean_string) == len(set(clean_string))