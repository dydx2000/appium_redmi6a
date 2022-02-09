import tkinter as tk


class Fullscreen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Example")
        self.fullScreenState = True
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))

        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        def room_button():
            room_text = room_key.get()
            print(room_text)

        def message_button():
            message_text = message.get(1.0, tk.END)
            handle_text = handle.get()
            print(message_text)
            print(handle_text)

        greeting = tk.Label(text="Welcome")
        # Pack displays the Label's text in the window.
        greeting.grid(column=1, sticky='w')

        display_room = tk.Label(text="Room:")
        display_room.grid(column=1, sticky='w')

        room_key = tk.Entry()
        room_key.grid(column=1, sticky='w')

        send_room_key = tk.Button(text="Change Rooms", command=room_button)
        send_room_key.grid(column=1, sticky='w')

        display_message = tk.Label(text="Message:")
        display_message.grid(column=1, sticky='w')

        message = tk.Text()
        message.grid(column=1, sticky='w')

        display_handle = tk.Label(text="Handle (optional):")
        display_handle.grid(column=1, sticky='w')

        handle = tk.Entry()
        handle.grid(column=1, sticky='w')

        send_message = tk.Button(text="Send Message", command=message_button)
        send_message.grid(column=1, sticky='w')

        quit_button = tk.Button(text="Quit", command=self.window.destroy)
        quit_button.grid(column=1, sticky='w')

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)


if __name__ == '__main__':
    app = Fullscreen()