#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
"""


"""
class NotesApplication(object):
    
    
    def __init__(self,author):
        self.author = author
        notes = []
        self.notes = notes
        
        
    def create(self, note_content):
        self.note_content = note_content
        self.notes.append(self.note_content)
        
    def list(self):
        
        for i in range(len(self.notes)):
            print "Note ID: %d" % i
            print self.get(i)
            print "By Author: %s" % self.author
            print ""
        
    def get(self,note_id):
        return self.notes[note_id]
    
    """
    
    def search(self, search_text):
        for text in search_text:
            for x in self.notes:
                s=x.split(' ')
                for value in s:
                    for v in value:
                        if text in v:
                            print x,"\n"
    
    """
    
    def search(self, search_text):
        print "Showing results for search '%s': \n" % search_text
        not_found = True
        for x in self.notes:
            if search_text in x:
                print "Note ID: %s" % self.notes.index(x)
                print x,"\n"
                not_found = False
        
        if not_found: 
            print "Found 0 matches"
        
    def edit(self, note_id, new_content):
        self.notes[note_id] = new_content

def main():
    note1 = NotesApplication("Paul")
    
    note1.create("Hello World")
    note1.create("Hello Pluto")
    note1.create("Jupiter Hello")
    
    m=raw_input('Enter the search string: ')
    note1.search(m)
        
    
    
if __name__ == "__main__":
    main()
