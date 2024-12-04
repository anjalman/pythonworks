class Editor:

    name:str

    ventor:str

    def __init__(self,name,vendor):

        self.name=name

        self.ventor=vendor

    def __str__(self):

        return self.name
    

editor_instance=Editor("pycharm","jebrains")

editor_instance2=Editor("intellij","jetbrains")

editor_instance3=Editor("vscode","microsoft")

print(editor_instance3)