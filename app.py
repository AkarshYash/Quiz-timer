import tkinter as tk
from tkinter import font
import pygame
import os
import math
import random

# Initialize pygame for sounds
pygame.mixer.init()

# Sound file paths (update these paths as needed)
timer_music = r"KBC Timer music_2_second level music for KBC..mp3"
correct_sound = "correct.wav"
wrong_sound   = "wrong.wav"
typing_sound = "typing.wav"  # Optional: add typing sound effect

# Global state
time_left = 60
timer_running = False
timer_id = None
particles = []  # For particle animation
blink_id = None  # To control the blinking cursor

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

# Typewriter animation for the headline
def typewriter_animation(text, label, index=0):
    if index < len(text):
        current_text = label.cget("text") + text[index]
        label.config(text=current_text)
        # Optional: play typing sound
        # if os.path.exists(typing_sound):
        #     pygame.mixer.Sound(typing_sound).play()
        screen.after(100, typewriter_animation, text, label, index+1)
    else:
        # Animation complete, add blinking cursor
        blink_cursor(label)

def blink_cursor(label):
    global blink_id
    current_text = label.cget("text")
    if current_text.endswith("|"):
        label.config(text=current_text[:-1])
    else:
        label.config(text=current_text + "|")
    blink_id = screen.after(500, blink_cursor, label)

def stop_blinking():
    global blink_id
    if blink_id:
        screen.after_cancel(blink_id)
        blink_id = None
    # Remove cursor from title
    current_text = title_label.cget("text")
    if current_text.endswith("|"):
        title_label.config(text=current_text[:-1])

# Particle animation for tech effect
def create_particles():
    global particles
    width = screen.winfo_width()
    height = screen.winfo_height()
    
    # Create new particles
    for _ in range(3):
        x = random.randint(0, width)
        y = random.randint(0, 100)  # Mostly in the top area
        size = random.randint(1, 3)
        speed = random.randint(1, 3)
        color = random.choice(["#0ff0fc", "#ff355e", "#00cc00", "#ffcc00"])
        direction = random.choice([-1, 1])
        particles.append({"x": x, "y": y, "size": size, "speed": speed, 
                         "color": color, "direction": direction})
    
    # Update and draw particles
    particle_canvas.delete("all")
    for particle in particles[:]:
        particle["x"] += particle["direction"] * particle["speed"]
        particle["y"] += particle["speed"]
        
        if (particle["x"] < 0 or particle["x"] > width or 
            particle["y"] < 0 or particle["y"] > height):
            particles.remove(particle)
        else:
            particle_canvas.create_oval(
                particle["x"], particle["y"], 
                particle["x"] + particle["size"], 
                particle["y"] + particle["size"],
                fill=particle["color"], outline=""
            )
    
    # Continue animation
    screen.after(50, create_particles)

# Glitch effect for headline
def glitch_effect(label, count=0):
    if count < 5:  # Number of glitches
        original_text = label.cget("text")
        # Create glitch text
        glitch_text = ""
        for char in original_text:
            if random.random() < 0.3:  # 30% chance to glitch each character
                glitch_text += random.choice("01!@#$%&*")
            else:
                glitch_text += char
        label.config(text=glitch_text)
        screen.after(100, glitch_effect, label, count+1)
    else:
        # Restore original text
        label.config(text="TECH QUIZATHON")

# Countdown logic
def countdown():
    global time_left, timer_running, timer_id
    if timer_running and time_left > 0:
        time_left -= 1
        update_timer_display()
        timer_id = screen.after(1000, countdown)
    elif time_left == 0:
        timer_label.config(text="⏰ TIME'S UP!", fg="#ff355e")
        stop_music()
        timer_running = False
        # Flash the timer
        flash_timer(3)

# Flash timer effect
def flash_timer(times):
    if times > 0:
        current_color = timer_label.cget("fg")
        new_color = "#ff355e" if current_color != "#ff355e" else "#0ff0fc"
        timer_label.config(fg=new_color)
        screen.after(500, flash_timer, times-1)

# Draw analog clock
def draw_clock():
    canvas.delete("all")
    width = 200
    height = 200
    center_x = width // 2
    center_y = height // 2
    radius = min(width, height) // 2 - 10
    
    # Draw clock face with tech design
    canvas.create_oval(center_x - radius, center_y - radius, 
                      center_x + radius, center_y + radius, 
                      outline="#0ff0fc", width=3, fill="#0c0c2e")
    
    # Draw circuit pattern inside clock
    for i in range(0, 360, 30):
        angle = math.radians(i)
        inner_radius = radius - 20
        x1 = center_x + inner_radius * math.sin(angle)
        y1 = center_y - inner_radius * math.cos(angle)
        x2 = center_x + (radius - 5) * math.sin(angle)
        y2 = center_y - (radius - 5) * math.cos(angle)
        canvas.create_line(x1, y1, x2, y2, fill="#0ff0fc", width=1, dash=(2, 2))
    
    # Draw hour markers
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = center_x + (radius - 10) * math.sin(angle)
        y1 = center_y - (radius - 10) * math.cos(angle)
        x2 = center_x + radius * math.sin(angle)
        y2 = center_y - radius * math.cos(angle)
        canvas.create_line(x1, y1, x2, y2, fill="#0ff0fc", width=2)
    
    # Draw minute markers
    for i in range(60):
        if i % 5 != 0:  # Skip where hour markers are
            angle = math.radians(i * 6)
            x1 = center_x + (radius - 5) * math.sin(angle)
            y1 = center_y - (radius - 5) * math.cos(angle)
            x2 = center_x + radius * math.sin(angle)
            y2 = center_y - radius * math.cos(angle)
            canvas.create_line(x1, y1, x2, y2, fill="#0ff0fc", width=1)
    
    # Draw numbers in tech style
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = center_x + (radius - 25) * math.cos(angle)
        y = center_y + (radius - 25) * math.sin(angle)
        canvas.create_text(x, y, text=str(i), fill="#0ff0fc", font=("Courier", 10, "bold"))
    
    # Draw center dot with glow effect
    canvas.create_oval(center_x - 6, center_y - 6, center_x + 6, center_y + 6, 
                      fill="#0ff0fc", outline="#0ff0fc")
    canvas.create_oval(center_x - 4, center_y - 4, center_x + 4, center_y + 4, 
                      fill="#0c0c2e", outline="#0c0c2e")

# Update timer display with clock visualization
def update_timer_display():
    timer_label.config(text=f"{time_left} SECONDS")
    
    # Update clock hands
    canvas.delete("hands")
    width = 200
    height = 200
    center_x = width // 2
    center_y = height // 2
    radius = min(width, height) // 2 - 10
    
    # Calculate hand angles
    seconds_angle = math.radians(360 * (time_left % 60) / 60 - 90)
    minutes_angle = math.radians(360 * (time_left // 60) / 60 - 90)
    
    # Draw second hand
    sec_x = center_x + (radius - 20) * math.cos(seconds_angle)
    sec_y = center_y + (radius - 20) * math.sin(seconds_angle)
    
    # Change color based on time left
    hand_color = "#0ff0fc" if time_left > 10 else "#ff355e"
    
    canvas.create_line(center_x, center_y, sec_x, sec_y, 
                      fill=hand_color, width=2, tags="hands", arrow=tk.LAST)
    
    # Draw minute hand
    min_x = center_x + (radius - 40) * math.cos(minutes_angle)
    min_y = center_y + (radius - 40) * math.sin(minutes_angle)
    canvas.create_line(center_x, center_y, min_x, min_y, 
                      fill=hand_color, width=4, tags="hands", arrow=tk.LAST)

# Start timer with animation
def start_timer():
    global time_left, timer_running
    if timer_id:
        screen.after_cancel(timer_id)
    time_left = 60
    timer_running = True
    timer_label.config(text=f"{time_left} SECONDS", fg="#0ff0fc")
    draw_clock()
    update_timer_display()
    
    # Add a visual effect when starting timer
    flash_border(5)
    play_music(timer_music, loop=True)
    countdown()

# Flash border effect
def flash_border(times):
    if times > 0:
        current_color = main_frame.cget("bg")
        new_color = "#0ff0fc" if current_color != "#0ff0fc" else "#0c0c2e"
        main_frame.config(bg=new_color)
        screen.after(200, flash_border, times-1)

# Reset everything
def reset_all():
    global time_left, timer_running
    if timer_id:
        screen.after_cancel(timer_id)
    stop_music()
    timer_running = False
    time_left = 60
    screen.config(bg="#0c0c2e")
    main_frame.config(bg="#0c0c2e")
    label.config(text="", bg="#0c0c2e", fg="#0ff0fc")
    timer_label.config(text=f"{time_left} SECONDS", fg="#0ff0fc")
    draw_clock()
    update_timer_display()

# Full screen color flash effect
def flash_fullscreen(color, duration=2000):
    # Create a full-screen overlay
    overlay = tk.Canvas(screen, bg=color, highlightthickness=0)
    overlay.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Remove overlay after duration
    screen.after(duration, overlay.destroy)

# Correct answer with animation
def correct():
    global timer_running
    if timer_id:
        screen.after_cancel(timer_id)
    timer_running = False
    stop_music()
    stop_blinking()
    
    # Flash the entire screen green
    flash_fullscreen("#00cc00", 2000)
    
    label.config(text="✅ CORRECT ANSWER!", fg="#0ff0fc", font=("Orbitron", 40, "bold"))
    play_effect(correct_sound)
    # Trigger glitch effect on headline
    glitch_effect(title_label)
    
    # Reset after animation
    screen.after(2000, reset_all)

# Wrong answer with animation
def wrong():
    global timer_running
    if timer_id:
        screen.after_cancel(timer_id)
    timer_running = False
    stop_music()
    stop_blinking()
    
    # Flash the entire screen red
    flash_fullscreen("#ff355e", 2000)
    
    label.config(text="❌ WRONG ANSWER!", fg="#0ff0fc", font=("Orbitron", 40, "bold"))
    play_effect(wrong_sound)
    # Trigger glitch effect on headline
    glitch_effect(title_label)
    
    # Reset after animation
    screen.after(2000, reset_all)

# Button hover effects
def on_enter(e, button, color):
    button.config(bg=color, relief=tk.RAISED)
    # Add a subtle glow effect
    button.config(highlightbackground=color, highlightcolor=color, highlightthickness=2)

def on_leave(e, button, color):
    button.config(bg=color, relief=tk.FLAT)
    # Remove glow effect
    button.config(highlightthickness=0)

# GUI setup
screen = tk.Tk()
screen.title("Tech Quizathon Buzzer")
screen.attributes('-fullscreen', True)
screen.config(bg="#0c0c2e")

# Custom fonts
try:
    title_font = font.Font(family="Orbitron", size=60, weight="bold")
    label_font = font.Font(family="Orbitron", size=40, weight="bold")
    button_font = font.Font(family="Orbitron", size=16, weight="bold")
    timer_font = font.Font(family="Orbitron", size=24, weight="bold")
except:
    title_font = font.Font(family="Helvetica", size=60, weight="bold")
    label_font = font.Font(family="Helvetica", size=40, weight="bold")
    button_font = font.Font(family="Helvetica", size=16, weight="bold")
    timer_font = font.Font(family="Helvetica", size=24, weight="bold")

# Main frame with gradient background
main_frame = tk.Frame(screen, bg="#0c0c2e")
main_frame.pack(fill=tk.BOTH, expand=True)

# Canvas for particle animation (behind everything)
particle_canvas = tk.Canvas(main_frame, bg="#0c0c2e", highlightthickness=0)
particle_canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Header with title
header = tk.Frame(main_frame, bg="#0c0c2e")
header.pack(pady=20)

# Tech Quizathon headline with typewriter animation
title_label = tk.Label(header, text="", font=title_font, 
                       fg="#0ff0fc", bg="#0c0c2e")
title_label.pack()

# Add digital effect underline
canvas_underline = tk.Canvas(header, width=600, height=5, bg="#0c0c2e", highlightthickness=0)
canvas_underline.pack()
for i in range(0, 600, 10):
    fill_color = "#0ff0fc" if i % 20 == 0 else "#ff355e"
    canvas_underline.create_rectangle(i, 0, i+5, 5, fill=fill_color, outline="")

# Timer section with analog clock
timer_frame = tk.Frame(main_frame, bg="#0c0c2e")
timer_frame.pack(pady=30)

# Canvas for analog clock
canvas = tk.Canvas(timer_frame, width=200, height=200, bg="#0c0c2e", 
                  highlightthickness=0)
canvas.pack()

timer_label = tk.Label(timer_frame, text="60 SECONDS", font=timer_font, 
                      bg="#0c0c2e", fg="#0ff0fc")
timer_label.pack(pady=10)

# Result label
label = tk.Label(main_frame, text="", font=label_font, bg="#0c0c2e", fg="#0ff0fc")
label.pack(pady=30, expand=True)

# Button frame
button_frame = tk.Frame(main_frame, bg="#0c0c2e")
button_frame.pack(side=tk.BOTTOM, pady=50)

# Style for buttons
button_style = {
    "font": button_font,
    "width": 16,
    "height": 2,
    "relief": tk.FLAT,
    "borderwidth": 0,
    "cursor": "hand2"
}

# Green button
green_button = tk.Button(button_frame, text="CORRECT", command=correct,
                         bg="#00cc00", fg="#0c0c2e", **button_style)
green_button.grid(row=0, column=0, padx=15, pady=10)
green_button.bind("<Enter>", lambda e: on_enter(e, green_button, "#00ff00"))
green_button.bind("<Leave>", lambda e: on_leave(e, green_button, "#00cc00"))

# Red button
red_button = tk.Button(button_frame, text="WRONG", command=wrong,
                       bg="#ff355e", fg="#0c0c2e", **button_style)
red_button.grid(row=0, column=1, padx=15, pady=10)
red_button.bind("<Enter>", lambda e: on_enter(e, red_button, "#ff0000"))
red_button.bind("<Leave>", lambda e: on_leave(e, red_button, "#ff355e"))

# Start button
start_button = tk.Button(button_frame, text="START TIMER", command=start_timer,
                         bg="#0ff0fc", fg="#0c0c2e", **button_style)
start_button.grid(row=0, column=2, padx=15, pady=10)
start_button.bind("<Enter>", lambda e: on_enter(e, start_button, "#00ffff"))
start_button.bind("<Leave>", lambda e: on_leave(e, start_button, "#0ff0fc"))

# Reset button
reset_button = tk.Button(button_frame, text="RESET", command=reset_all,
                         bg="#ffcc00", fg="#0c0c2e", **button_style)
reset_button.grid(row=0, column=3, padx=15, pady=10)
reset_button.bind("<Enter>", lambda e: on_enter(e, reset_button, "#ffff00"))
reset_button.bind("<Leave>", lambda e: on_leave(e, reset_button, "#ffcc00"))

# Exit button
exit_button = tk.Button(button_frame, text="EXIT", command=screen.destroy,
                       bg="#8b00ff", fg="#ffffff", **button_style)
exit_button.grid(row=0, column=4, padx=15, pady=10)
exit_button.bind("<Enter>", lambda e: on_enter(e, exit_button, "#aa00ff"))
exit_button.bind("<Leave>", lambda e: on_leave(e, exit_button, "#8b00ff"))

# Start animations
typewriter_animation("TECH QUIZATHON", title_label)
create_particles()
draw_clock()
update_timer_display()

screen.mainloop()