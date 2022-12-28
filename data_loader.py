import os
import re
import discord

title_regex = "^@."

def get_contents(key_dict):
   """
      Returns a list of topics
   """
   out_str = ""
   for line in key_dict.keys():
      out_str += line + "\n"
   return out_str
      
##################################################
# text parser. 

class input_text_parser:
   def __init__(self, dir_path):
      self.dict = {}       # case-sensitive dict
      self.key_dict = {}   # pairs of (key.lower, key)
      self.topic_list = ""
      file_list = os.listdir(dir_path)
      for f in file_list:
         self._load(dir_path, f)
      self.topic_list = self.topic_list.strip()
   
   def _load(self, dir_path, file_name):
      content_string = ""
      content_category = file_name.split('.')[0]
      content_list = ""
      try:
         with open(f"{dir_path}/{file_name}", "r") as file:
            content_string = file.read()
         # trim input to start at first entry name
         line_list = content_string.split("\n")
         i = 0
         while not re.search(title_regex, line_list[i]):
            i += 1
         line_list = line_list[i:]
         
         # create and populate individual entries
         title = ""
         text = ""
         for line in line_list:
            if re.search(title_regex, line):
               if title != "" and text != "":
                  self._add_item(title, text)
                  content_list += f"{title}\n"
               title = line[1:].strip()
               text = ""
            else:
               text = text + line.strip() + "\n"
         if title != "" and text != "":
            self._add_item(title, text)
            content_list += f"{title}\n"
         # add category to common list
         self.dict[content_category] = content_list.strip()
         self.key_dict[content_category.lower()] = content_category
         # add category to master list
         self.topic_list += f"{content_category}\n"
      except Exception as ex:
         print(ex)
   
   def _add_item(self, title, text):
      """
      Add item to dict and key dict
      """
      self.dict[title] = text.strip()
      self.key_dict[title.lower()] = title
   
   def get(self, outer_key):
      """
      Returns the value for the key, or None if no such key
      """
      inner_key = self.key_dict.get(outer_key.lower())
      return self.dict.get(inner_key)
   
   def get_contents(self):
      """
      Returns a table of contents.
      """
      return self.topic_list.strip()

##################################################
# image parser. Well, general file, really.

class input_image_parser:
   def __init__(self, dir_path):
      self.dict = {}       # pairs of (name, dir/name.ext)
      self.key_dict = {}   # pairs of (key.lower, key)
      file_list = os.listdir(dir_path)
      for f in file_list:
         key = f.split(".")[0]
         self.dict[key] = f"{dir_path}/{f}"
         self.key_dict[key.lower()] = key
   
   def get(self, outer_key):
      """
      Returns the file for the key, or None if no such key
      """
      inner_key = self.key_dict.get(outer_key.lower())
      file_name = self.dict.get(inner_key)
      if file_name != None:
         with open(file_name, 'rb') as f:
            return discord.File(f)
      return None
   
   def get_contents(self):
      """
      Returns a table of contents.
      """
      key_arr = self.dict.keys()
      out_str = ""
      for element in key_arr:
         out_str += f"{element}\n"
      return out_str.strip()


if __name__ == "__main__":
#    reader = input_text_parser("./text")
#    print(reader.dict.keys())
#    print(reader.dict.values())
#    print(reader.key_dict.keys())
#    print(reader.key_dict.values())
#    print(reader.get("first thing"))
#    print(reader.get("pants"))
#    print(reader.get("FiRsT tHiNg"))
  # toc = reader.get_contents()
   #print(reader.get("first thing"))
#    print(reader.get_contents())
#    print(reader.get("category 1"))
   # 
   reader = input_image_parser("./images")
   print(reader.dict.keys())
   print(reader.dict.values())
   print(reader.get("ricci"))
   print(reader.get_contents())