class Person():
    def __init__(self, name):
        self._name = name

    @property  # Getter 메서드 정의
    def name(self) -> str:
        return self._name
    
    
    def hello(self):
        print(self._name)
