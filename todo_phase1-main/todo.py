"""
Todo App - Phase 1
Console Based | In-Memory Storage
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Todo:
    id: int
    title: str
    description: str
    completed: bool = False

class TodoApp:
    def __init__(self):
        self.todos: List[Todo] = []
        self.next_id = 1

    def _find_by_id(self, todo_id: int) -> Optional[Todo]:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def _input_id(self) -> Optional[int]:
        try:
            return int(input("Enter Todo ID: "))
        except ValueError:
            print("❌ Invalid ID")
            return None

    def add_todo(self):
        print("\n➕ ADD TODO")
        title = input("Title: ").strip()
        desc = input("Description: ").strip()
        if not title:
            print("❌ Title required")
            return
        self.todos.append(Todo(self.next_id, title, desc))
        self.next_id += 1
        print("✅ Todo added")

    def view_all(self):
        if not self.todos:
            print("📭 No todos")
            return
        print("\n📋 TODOS")
        for t in self.todos:
            status = "✔ Completed" if t.completed else "❌ Pending"
            print(f"[{t.id}] {t.title} - {t.description} ({status})")

    def update_todo(self):
        print("\n✏️ UPDATE TODO")
        tid = self._input_id()
        if tid is None: return
        todo = self._find_by_id(tid)
        if not todo:
            print("❌ Todo not found")
            return
        new_title = input("New title (leave blank to keep same): ").strip()
        new_desc = input("New description (leave blank to keep same): ").strip()
        if new_title: todo.title = new_title
        if new_desc: todo.description = new_desc
        print("✅ Updated")

    def delete_todo(self):
        print("\n🗑 DELETE TODO")
        tid = self._input_id()
        if tid is None: return
        todo = self._find_by_id(tid)
        if not todo:
            print("❌ Todo not found")
            return
        confirm = input("Confirm delete (y/n): ").lower()
        if confirm == "y":
            self.todos.remove(todo)
            print("✅ Deleted")
        else:
            print("❎ Cancelled")

    def toggle_status(self):
        print("\n🔄 CHANGE STATUS")
        tid = self._input_id()
        if tid is None: return
        todo = self._find_by_id(tid)
        if not todo:
            print("❌ Todo not found")
            return
        todo.completed = not todo.completed
        state = "Completed" if todo.completed else "Pending"
        print(f"✅ Todo marked as {state}")

def show_menu():
    print("\n=== TODO APP ===")
    print("1. Add Todo")
    print("2. View All Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Complete / Incomplete")
    print("6. Exit")

def main():
    app = TodoApp()
    while True:
        show_menu()
        choice = input("Choose option (1-6): ").strip()
        if choice == "1": app.add_todo()
        elif choice == "2": app.view_all()
        elif choice == "3": app.update_todo()
        elif choice == "4": app.delete_todo()
        elif choice == "5": app.toggle_status()
        elif choice == "6":
            print("👋 Bye"); break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
