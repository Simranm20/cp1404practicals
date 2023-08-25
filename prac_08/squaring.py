"""
CP1404/CP5632 Practical 8
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 150)
        self.title = "Square Number"

        root = BoxLayout(orientation='vertical')

        # Top section
        top_section = BoxLayout(orientation='horizontal')

        input_label = Label(text="Enter a number:", color=(1, 0, 1, 1))  # Pink color (RGBA)
        top_section.add_widget(input_label)

        self.input_number = TextInput()
        top_section.add_widget(self.input_number)

        calculate_button = Button(text="Square")
        calculate_button.bind(on_press=self.handle_calculate)  # Bind the function to the button's on_press event
        top_section.add_widget(calculate_button)

        root.add_widget(top_section)

        # Bottom section
        output_label = Label(text="Enter a number and press 'Square'", color=(1, 0, 1, 1), size_hint_y=None,
                             height=30)  # Pink color (RGBA)
        root.add_widget(output_label)

        self.output_label = output_label  # Store a reference to the output label

        return root

    def handle_calculate(self, instance):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            value = float(self.input_number.text)
            result = value ** 2
            self.output_label.text = f"Result: {result}"
        except ValueError:
            self.output_label.text = "Invalid input"


if __name__ == '__main__':
    SquareNumberApp().run()
