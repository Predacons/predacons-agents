
import nbformat
from nbclient import NotebookClient
class PythonNotebook:
    def __init__(self):
        self.nb = nbformat.v4.new_notebook()

    def add_code_cell(self, code):
        self.nb.cells.append(nbformat.v4.new_code_cell(code))
        # Return the index of the cell
        return len(self.nb.cells) - 1

    def execute(self):
        client = NotebookClient(self.nb)
        client.execute()
        return self.nb

    def execute_cell(self, cell_index):
        client = NotebookClient(self.nb)
        client.execute_cell(cell_index=cell_index)
        return self.nb.cells[cell_index]

    def save(self, file_path):
        with open(file_path, "w") as f:
            nbformat.write(self.nb, f)