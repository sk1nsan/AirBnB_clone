from models.engine.file_storage import FileStorage

""" importing file storage  to create a unique FileStorage
 instance for the application"""

storage = FileStorage()
storage.reload()
