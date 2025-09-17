# 🎯 Tech Quizathon Buzzer

An **interactive Quiz Buzzer System** built with **Python (Tkinter + Pygame)** featuring:

✅ Countdown Timer with Analog Clock
✅ Typewriter & Glitch Effects
✅ Particle Background Animation
✅ Fullscreen Visual Feedback (Green for Correct, Red for Wrong)
✅ Tech-Themed UI with Hover Effects
✅ Sound Integration (Timer, Correct, Wrong, Typing)
✅ Reset & Exit Controls

Perfect for **quiz competitions, hackathons, or college fests** 🎤

---

## 🖼️ Demo Preview

*(Add screenshots or GIFs here of the running app, e.g. showing the timer, buttons, and animations.)*

---

## ⚙️ Features

* 🎬 **Typewriter Animation** → Stylish animated heading with blinking cursor
* ⚡ **Glitch Effect** → Headline glitches like a cyberpunk interface
* ⏳ **60-Second Timer** → Digital + Analog clock countdown
* 🎶 **Sound System**

  * Timer background music (loops)
  * Correct answer sound effect
  * Wrong answer sound effect
  * Optional typing sound effect
* 🌌 **Particle Animation** → Floating neon particles on the background
* 🟢 **Correct Answer Animation** → Screen flashes green + glitch effect
* 🔴 **Wrong Answer Animation** → Screen flashes red + glitch effect
* 🖥️ **Hover Effects** → Buttons glow when hovered
* 🎨 **Cyberpunk Theme** → Orbitron font + neon color palette

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Tkinter** → GUI framework
* **Pygame** → Sound & music playback
* **Math & Random** → Animations & effects
* **Custom Fonts (Orbitron)** → Futuristic look

---

## 📂 Project Structure

```
📁 Tech-Quizathon-Buzzer
│── quizathon_buzzer.py   # Main script
│── KBC Timer music_2_second level music for KBC..mp3  # Timer music
│── correct.wav           # Correct answer sound
│── wrong.wav             # Wrong answer sound
│── typing.wav            # Typing sound (optional)
│── README.md             # Project documentation
```

---

## 🚀 Installation & Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/Tech-Quizathon-Buzzer.git
   cd Tech-Quizathon-Buzzer
   ```

2. Install dependencies:

   ```bash
   pip install pygame
   ```

3. Run the app:

   ```bash
   python quizathon_buzzer.py
   ```

---

## 🎮 Controls

* ▶️ **Start Timer** → Begins countdown with animations & music
* ✅ **Correct** → Flashes green + sound + reset
* ❌ **Wrong** → Flashes red + sound + reset
* 🔄 **Reset** → Stops everything & resets timer to 60s
* ⏹️ **Exit** → Quit the app

---

## 🎨 Customization

* Replace `timer_music`, `correct_sound`, `wrong_sound`, `typing_sound` with your own files.
* Change **colors** in the script (`#0ff0fc`, `#ff355e`, etc.) for a new theme.
* Adjust **time\_left** to change the countdown duration.
* Modify **fonts** if Orbitron is not installed (default falls back to Helvetica).

---

## 🤝 Contribution

Feel free to fork, enhance animations, add buzzers for multiple teams, or integrate with hardware buzzers.
PRs are welcome 💡
