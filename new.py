#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def tokenize(text):
    # Split the text into words using regular expression
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# Example usage:
text = "This is a sample sentence for tokenization. It demonstrates basic tokenization."
tokens = tokenize(text)
print(tokens)


# In[ ]:




