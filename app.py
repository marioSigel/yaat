import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np
from tkinter import ttk
import os
from db.access import get_con, save_results, get_completed_list

scale_factor = 2
img_dir = './images'
bbox = 300


class MainWindow():

    def __init__(self, window):
        self.con = get_con()
        file_list = os.listdir(img_dir)
        completed_list = get_completed_list(self.con)
        self.file_list = [n for n in file_list if n not in completed_list]

        self.img_id = 0
        self.load_img(self.c_file_path())

        self.w = tkinter.Label(window, text=self.c_file_name())
        self.w.pack()
        self.canvas = tkinter.Canvas(window, width = self.width, height = self.height, borderwidth=-4)
        self.canvas.bind("<Button-1>", self.callback_click)
        self.canvas.bind("<ButtonRelease-1>", self.callback_click_release)
        self.canvas.bind("<B1-Motion>", self.callback_mouse_moved)
        self.canvas.pack()

        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.tk_img = self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.btn = ttk.Button(window, text="Save and next", width=30, command=self.next_img)
        self.btn.pack(anchor=tkinter.CENTER, expand=True)

        self.btn = ttk.Button(window, text="Reset selection", width=30, command=self.reset)
        self.btn.pack(anchor=tkinter.CENTER, expand=True)

        self.btn = ttk.Button(window, text="Discard (e.g. complete cloud) and next", width=30, command=self.discard)
        self.btn.pack(anchor=tkinter.CENTER, expand=True)

        self.p1 = None
        self.p2 = None

    def c_file_name(self):
        name = self.file_list[self.img_id] if self.file_list and self.img_id < len(self.file_list) else None

        if name is None:
            print('Done.')
            exit()
        return name

    def c_file_path(self):
        name = self.c_file_name()
        return os.path.join(img_dir, name)

    def load_img(self, img_path):
        self.cv_img = cv2.imread(img_path)

        self.cv_img = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2RGB)
        self.cv_img = cv2.resize(self.cv_img,(int(self.cv_img.shape[1] * scale_factor), int(self.cv_img.shape[0] * scale_factor)))

        self.height, self.width, self.no_channels = self.cv_img.shape

    def callback_click(self, event):
        # print("clicked at", event.x, event.y)
        self.p1 = (event.x, event.y)
        self.p2 = None

    def callback_mouse_moved(self, event):
        # print("moved", event.x, event.y)
        self.p2 = (event.x, event.y)
        self.update_image()

    def callback_click_release(self, event):
        # print("released at", event.x, event.y)
        self.p2 = (event.x, event.y)
        self.update_image()

    def update_image(self):
        if self.p1 is not None and self.p2 is not None:
            display_img = np.copy(self.cv_img)
            cv2.rectangle(display_img, self.p1, self.p2, (255, 0, 0))

            self.update_canvas(display_img)

    def update_canvas(self, cv_img):
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        self.canvas.itemconfig(self.tk_img, image=self.photo)

    def continue_with_next_im(self):
        self.p1 = None
        self.p2 = None

        self.img_id += 1
        self.load_img(self.c_file_path())
        self.update_canvas(self.cv_img)

    def next_img(self):
        x1, y1, x2, y2 = [min(max(int(v / scale_factor), 0), bbox) for v in [*self.p1, *self.p2]] \
            if self.p1 and self.p2 else (None,) * 4
        save_results(self.con, self.c_file_name(), False, x1, y1, x2, y2)
        self.continue_with_next_im()

    def discard(self):
        save_results(self.con, self.c_file_name(), True, *(None,) * 4)
        self.continue_with_next_im()

    def reset(self):
        self.p1 = None
        self.p2 = None

        self.update_canvas(self.cv_img)


if __name__ == '__main__':
    window = tkinter.Tk()
    MainWindow(window)
    window.mainloop()
