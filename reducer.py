#!/usr/bin/env python
def reducer():

    current_president = None
    total_valence = 0
    word_count = 0
   
    for line in sys.stdin:
        #line = line.strip()
        president_name, word_valence = line.split('\t')
        word_valence = int(word_valence)
        
        if current_president == president_name:
                # Accumulate valence and count words
                total_valence += word_valence
                word_count += 1
        else:
            if current_president:
                # Emit the average valence for the previous president
                avg_valence = total_valence / word_count if word_count > 0 else 0
                print(f"{current_president}\t{avg_valence}")

            # Update the current president
            current_president = president_name
            total_valence = word_valence
            word_count = 1
    if current_president:
            avg_valence = total_valence / word_count
            print(f"{current_president}\t{avg_valence}") if word_count > 0 else 0
            #print('Finished  processing filename and total speeches:', filename, i)
