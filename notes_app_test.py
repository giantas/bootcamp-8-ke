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


if __name__ == '__main__':
    unittest.main()
