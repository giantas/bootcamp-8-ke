# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import notes_application
import unittest


class  NotesAppTestCase(unittest.TestCase):
    
    #def test_list_when_index_is_one(self):
    #    self.assertEqual(notes_application.list(1),tuple() )
    def setUp(self):
        self.note = notes_application.NotesApplication("Paul")
    
    def test_num_of_notes(self):
        self.assertEqual(self.note.num_of_notes(), 0)
    
    def test_note_creation(self):
        self.note.create("This is a test value")
        self.assertIsNotNone(self.note.num_of_notes())
    
    def test_get_note_content_by_id(self):
        self.note.create("This is a test value")
        self.assertEqual(self.note.get(0), "This is a test value")
    
    def test_note_editing(self):
        self.note.create("This is a test value")
        first_value = self.note.get(0)
        self.note.edit(0,"Value has changed")
        second_value = self.note.get(0)
        self.assertNotEqual(first_value, second_value)


if __name__ == '__main__':
    unittest.main()
