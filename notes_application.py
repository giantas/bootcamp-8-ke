#!/usr/bin/env python2
#encoding: UTF-8

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
            print "\nNote ID: %d" % i
            print self.get(i)
            print "By Author: %s" % self.author
            print ""
        
    def get(self,note_id):
        return self.notes[note_id]
      
    def search(self, search_text):
        print "Showing results for search '%s': " % search_text
        for note in self.notes:
            if search_text in note:
                print "\nNote ID: %s" % self.notes.index(note)
                print note
                print "By Author: %s" % self.author
        """
        if not_found: 
            print "Found 0 matches"
        """
    
    def num_of_notes(self):
        return len(self.notes)
    
    def edit(self, note_id, new_content):
        self.notes[note_id] = new_content

def main():
    auth_name = raw_input("Enter note author: ")
    note1 = NotesApplication(auth_name)
    
    choice = raw_input("\nSelect you preferred option: \n\t1. Add note\n\t2. Search string\n\t3. Edit note\n\t4. Print notes\n\t5. Exit\nSelection: ")
    
    while choice is not '4':
        if choice == '1':
            new_note = raw_input("Enter note content: ")
            note1.create(new_note)
            print "Note added!\n"
        elif choice == '2':
            search_string = raw_input('Enter the search string: ')
            note1.search(search_string)
        elif choice == '3':
            if note1.num_of_notes() == 0:
                print "\nAdd note first!"
            else:
                id_input = raw_input("Enter Note ID: ")
                note_edit = raw_input("Enter note content: ")
                note1.edit(id_input,note_edit)
                print "Note edited!"
        elif choice == '4':
            if note1.num_of_notes() == 0:
                print "No notes found here"
            else:
                note1.list()
        elif choice == '5':
            print "Goodbye!"
            exit()
        else:
            print "Incorrect selection. (use the numbers)"
            
        choice = raw_input("\nSelect you preferred option: \n\t1. Add note\n\t2. Search string\n\t3. Edit note\n\t4. Print notes\n\t5. Exit\nSelection: ")
        
    
if __name__ == "__main__":
    main()