import os
import io
import json
import tempfile
import unittest
import shutil
import pickle
import warnings
from document import Document, DocumentManager  
from user import User
from settings import EditorSettings, HistoryManager
from storage import LocalStorageStrategy, SQLiteStorageStrategy, CloudStorageStrategy
    
class TestDocumentFunctionality(unittest.TestCase):
    def setUp(self):
        
        self.owner = User("owner")
        self.editor = User("editor")
        
        self.doc = Document(title="TestDoc", content="Initial content", owner=self.owner)
    
    def test_document_creation(self):
        self.assertEqual(self.doc.title, "TestDoc")
        self.assertEqual(self.doc.content, "Initial content")
        self.assertTrue(self.doc.is_open)
    
    def test_edit_notification(self):
        
        self.doc.edit(self.editor, "Updated content by editor")
        self.assertEqual(self.doc.content, "Updated content by editor")
        self.assertGreater(len(self.owner.notifications), 0)
        note = self.owner.notifications[0]
        self.assertIn("TestDoc", note)
        self.assertIn("editor", note)
    
    def test_edit_by_owner_no_notification(self):
        
        self.doc.edit(self.owner, "Owner updated content")
        self.assertEqual(self.doc.content, "Owner updated content")
        self.assertEqual(len(self.owner.notifications), 0)

class TestLocalStorageStrategy(unittest.TestCase):
    def setUp(self):
        
        self.test_dir = tempfile.mkdtemp()
        
        self.local_strategy = LocalStorageStrategy(folder=self.test_dir)
        self.doc = Document(title="LocalTest", content="Some local content", owner=User("owner"))
    
    def test_local_save_txt(self):
        self.local_strategy.save(self.doc, "TXT")
        file_path = os.path.join(self.test_dir, "LocalTest.txt")
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, "Some local content")
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)







    












    




class TestEditorSettingsHistory(unittest.TestCase):
    def setUp(self):
        self.settings = EditorSettings()
        self.history_manager = HistoryManager()
        
        self.history_manager.history.clear()
    
    def test_editor_settings(self):
        
        self.assertEqual(self.settings.theme, "Светлая")
        self.assertEqual(self.settings.font_size, 12)
        self.settings.set_theme("Тёмная")
        self.settings.set_font_size(16)
        self.assertEqual(self.settings.theme, "Тёмная")
        self.assertEqual(self.settings.font_size, 16)
    
    def test_history_manager(self):
        self.history_manager.add_entry("Doc1", "owner", "создан")
        self.history_manager.add_entry("Doc1", "editor", "отредактирован")
        history = self.history_manager.view_history()
        self.assertEqual(len(history), 2)
        self.assertIn("Doc1", history[0]["document"])
        self.assertIn("editor", history[1]["user"])

@unittest.skip("Google Drive тесты требуют реальных credentials и интерактивной авторизации.")
class TestGoogleDriveStorageStrategy(unittest.TestCase):
    def test_google_drive_save(self):
        
        strategy = CloudStorageStrategy(credentials_path='credentials.json', token_path='token_test.pickle')
        doc = Document(title="GDriveTest", content="Content for Google Drive test", owner=User("owner"))
        strategy.save(doc, "JSON")
        

@unittest.skip("File.io тесты можно выполнить только при корректном API, поэтому тест пропущен.")
class TestFileIoStorageStrategy(unittest.TestCase):
    def test_fileio_save(self):
        strategy = CloudStorageStrategy()
        doc = Document(title="FileIoTest", content="Content for file.io test", owner=User("owner"))
        strategy.save(doc, "TXT")
        
        

if __name__ == '__main__':
    
    warnings.simplefilter("ignore")
    unittest.main()
