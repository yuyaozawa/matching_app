class StopWatchApp(App):
    def build(self):
        layout = BoxLayout()
        layout.lbl = MyLabel(text='0')
        layout.btn = MyButton(text='start')
        layout.add_widget(layout.lbl)
        layout.add_widget(layout.btn)
        return layout
StopWatchApp().run()

