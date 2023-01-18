
def virus_project():

    import cv2
    from tkinter import Tk, Label
    from PIL import Image, ImageTk
    import pyautogui
    from vlc import MediaPlayer
    from  pyautogui import click

    video_path = 'C:\\mandala.mp4'

    cap = cv2.VideoCapture(video_path)

    #tkinter penceresi açma
    window = Tk()
    pyautogui.FAILSAFE = False
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.attributes("-fullscreen", True)
    window.title("System Hacked")
    window.config(bg='black')

    frame = Label(window)
    frame.pack()

    #ses dosyasını oynatma
    player_audio = MediaPlayer("C:\\Users\\LENOVO\\OneDrive\\Masaüstü\\techno.mp3")
    player_audio.play()


    #videonun oynatıldığı fonksiyon
    def update_frame():
        ret, frame_img = cap.read()

        frame_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_img)
        img = ImageTk.PhotoImage(img)

        frame.config(image=img)
        frame.img = img
        window.after(int(1000/cap.get(5)), update_frame)

    #klavyede herhangi bir tuşa basıldığında çalışmaması ve fare imlecinin hep ortya gitmesini sağlayan fonksiyon
    def on_closing():
        click(width / 2, height / 2)
        # moveTo(width / 2, height / 2)

        window.attributes("-fullscreen", True)

        window.protocol("WM_DELETE_WINDOW", on_closing)
        window.update()

    k = False

    update_frame()


    # 40 saniye sonra ekranı kapatan kod
    window.after(40000, window.destroy)
    while not k:
        on_closing()
    window.mainloop()




