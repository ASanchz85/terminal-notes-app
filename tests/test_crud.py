import pytest
import os

from CRUD.crud_operations import CRUD_management
from CRUD.notes import Note


@pytest.fixture
def crud_manager():
    """Fixture to create a temporary CRUD manager with an isolated file."""
    manager = CRUD_management("test_notes.pkl")
    yield manager
    if os.path.exists("test_notes.pkl"):
        os.remove("test_notes.pkl")


def test_add_note_and_read_all(crud_manager):
    """Test adding a note and reading all notes."""
    crud_manager.add_note("Test Title", "Test Content")
    notes = crud_manager.read_all_notes()
    assert len(notes) == 1
    assert notes[0].note_data["title"] == "Test Title"
    assert notes[0].note_data["content"] == "Test Content"


def test_search_note_by_title(crud_manager):
    """Test searching notes by title."""
    crud_manager.add_note("Python", "Programming language")
    crud_manager.add_note("Pytest", "Testing framework")
    results = crud_manager.search_note_by_title("Python")
    assert len(results) == 1
    assert results[0].note_data["title"] == "Python"


def test_search_note_by_content(crud_manager):
    """Test searching notes by content."""
    crud_manager.add_note("Learning", "Python programming basics")
    crud_manager.add_note("Advanced", "Deep learning concepts")
    results = crud_manager.search_note_by_content("Python")
    assert len(results) == 1
    assert results[0].note_data["content"] == "Python programming basics"


def test_delete_note_by_valid_index(crud_manager):
    """Test deleting a note by a valid index."""
    crud_manager.add_note("To Delete", "This note will be deleted")
    initial_count = len(crud_manager.read_all_notes())
    crud_manager.delete_note_by_title(0)
    assert len(crud_manager.read_all_notes()) == initial_count - 1


def test_delete_note_by_invalid_index(crud_manager):
    """Test deleting a note by an invalid index, expecting a ValueError."""
    crud_manager.add_note("Sample", "This is a sample note")
    with pytest.raises(ValueError, match="Invalid index"):
        crud_manager.delete_note_by_title(10)


def test_file_creation_and_loading():
    """Test that the file is created and data persists when reloaded."""
    manager1 = CRUD_management("test_persistence.pkl")
    manager1.add_note("Persistent Title", "Persistent Content")
    del manager1

    manager2 = CRUD_management("test_persistence.pkl")
    notes = manager2.read_all_notes()
    assert len(notes) == 1
    assert notes[0].note_data["title"] == "Persistent Title"
    assert notes[0].note_data["content"] == "Persistent Content"

    if os.path.exists("test_persistence.pkl"):
        os.remove("test_persistence.pkl")
