lexicon_list = [("direction", ["north", "south", "east", "west", "down", "up", "left", "right", "back"]), 
                ("verb", ["go", "stop", "kill", "eat"]),
                ("noun", ["bear", "door", "princess", "cabinet"]),
                ("article", ["the", "a", "an"]),
                ("preposition", ["on", "in", "from", "since", "at", "to", "for", "by"])]

def scan(entry):
    
    result = []           
    words_entry = entry.split()
        
    for word in words_entry: 
        
        if word.isalpha():            
            found_match = False
                    
            for sentence_part, words in lexicon_list:             
                if word.lower() in words:
                    result.append((sentence_part, word))
                    found_match = True
        
            if found_match is False:
                result.append(("error", word))  
                
        elif word.isdigit():                      
            try:
                result.append(("number", int(word)))
                
            except ValueError:
                 result.append(("error", word))                
                    
        else:                            
            result.append(("error", word))                
        
    return result
