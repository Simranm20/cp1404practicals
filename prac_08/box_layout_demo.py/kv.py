BoxLayout:
    orientation: 'vertical'
#    orientation: 'horizontal'
    Button:
        text: 'Clear'
    TextInput:
        id: input_name
        text: ''
    Button:
        text: 'Greet'
        on_press: app.handle_greet()
    Label:
        id: output_label
        text: 'Enter your name'
        # yellow
        color: (1, 1, 0, 1)