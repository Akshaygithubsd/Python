# print('''Twinkle, Twinkle,
#        Little Star" is an English lullaby.
#        The lyrics are from an early-19th-century English poem written by Jane Taylor,
#        "The Star".[1] The poem, which is in couplet form, 
#       was first published in 1806 in Rhymes for the Nursery, 
#       a collection of poems by Taylor and her sister Ann. It is now sung to the tune of the French melody "Ah! vous dirai-je, maman", which was first published in 1761 and later arranged by several composers, including Mozart with Twelve Variations on "Ah vous dirai-je, Maman".[2] The English lyrics have five stanzas, although only the first is widely known.''')


import pyttsx3
#pyhton text to speech module
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()