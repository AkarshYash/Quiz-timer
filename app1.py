import tkinter as tk
import pygame
import os

# Initialize pygame for sounds
pygame.mixer.init()

# Sound file paths
timer_music = r"KBC Timer music_2_second level music for KBC..mp3"
correct_sound = "correct.wav"
wrong_sound   = "wrong.wav"

# Global state
time_left = 60
timer_running = False

# Function to play music/sound
def play_music(file, loop=False):
    if os.path.exists(file):
        pygame.mixer.music.load(file)
        if loop:
            pygame.mixer.music.play(-1)  # loop forever
        else:
            pygame.mixer.music.play()
    else:
        print(f"[!] File not found: {file}")

def play_effect(file):
    if os.path.exists(file):
        sound = pygame.mixer.Sound(file)
        sound.set_volume(1.0)
        sound.play()
    else:
        print(f"[!] File not found: {file}")

def stop_music():
    pygame.mixer.music.stop()

# Countdown logic
def countdown():
    global time_left, timer_running
    if timer_running and time_left > 0:
        time_left -= 1
        timer_label.config(text=f"⏳ {time_left} sec")
        screen.after(1000, countdown)
    elif time_left == 0:
        timer_label.config(text="⏰ Time's Up!", fg="yellow")
        stop_music()
        timer_running = False

# Start timer
def start_timer():
    global time_left, timer_running
    time_left = 60
    timer_running = True
    timer_label.config(text=f"⏳ {time_left} sec", fg="white")
    play_music(timer_music, loop=True)
    countdown()

# Reset everything
def reset_all():
    global time_left, timer_running
    stop_music()
    timer_running = False
    time_left = 60
    screen.config(bg="black")
    label.config(text="", bg="black")
    timer_label.config(text=f"⏳ {time_left} sec", fg="white")

# Correct answer
def correct():
    global timer_running
    timer_running = False
    stop_music()
    screen.config(bg="green")
    label.config(text="✅ Correct Answer!", fg="white", bg="green", font=("Arial", 40, "bold"))
    play_effect(correct_sound)
    screen.after(3000, reset_all)

# Wrong answer
def wrong():
    global timer_running
    timer_running = False
    stop_music()
    screen.config(bg="red")
    label.config(text="❌ Wrong Answer!", fg="white", bg="red", font=("Arial", 40, "bold"))
    play_effect(wrong_sound)
    screen.after(3000, reset_all)

# GUI setup
screen = tk.Tk()
screen.title("Quizathon Buzzer")
screen.attributes('-fullscreen', True)
screen.config(bg="black")

# Timer label (BIGGER SIZE NOW)
timer_label = tk.Label(screen, text="⏳ 60 sec", font=("Arial", 70, "bold"), bg="black", fg="white")
timer_label.pack(pady=20)

# Result label
label = tk.Label(screen, text="", font=("Arial", 30, "bold"), bg="black", fg="white")
label.pack(expand=True)

# Button frame
frame = tk.Frame(screen, bg="black")
frame.pack(side="bottom", pady=50)

# Green button
green_button = tk.Button(frame, text="✅ Green (Correct)", command=correct,
                         font=("Arial", 20, "bold"), bg="green", fg="white", width=20, height=3)
green_button.grid(row=0, column=0, padx=20)

# Red button
red_button = tk.Button(frame, text="❌ Red (Wrong)", command=wrong,
                       font=("Arial", 20, "bold"), bg="red", fg="white", width=20, height=3)
red_button.grid(row=0, column=1, padx=20)

# Start timer button
start_button = tk.Button(frame, text="▶ Start Timer", command=start_timer,
                         font=("Arial", 20, "bold"), bg="blue", fg="white", width=20, height=3)
start_button.grid(row=0, column=2, padx=20)

# 🔥 Reset button (NEW)
reset_button = tk.Button(frame, text="🔄 Reset", command=reset_all,
                         font=("Arial", 20, "bold"), bg="orange", fg="white", width=20, height=3)
reset_button.grid(row=0, column=3, padx=20)

# Escape to quit
screen.bind("<Escape>", lambda e: screen.destroy())

screen.mainloop()
