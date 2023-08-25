from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = BoxLayout(orientation='vertical')
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            label = Label(text=name)
            self.root.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
