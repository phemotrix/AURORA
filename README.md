# 🌌 Aurora Music — Immersive Glass Audio Player

> A desktop-optimized, Apple Music-inspired glassmorphic audio player built for 100% offline local listening and instant **GitHub Pages** deployment with zero build steps.

![Aurora Player](https://img.shields.io/badge/Deploy-GitHub_Pages-blue?style=for-the-badge&logo=github)
![Offline PWA](https://img.shields.io/badge/Storage-IndexedDB_100%25_Offline-00d2ff?style=for-the-badge)
![Web Audio](https://img.shields.io/badge/Audio-60FPS_Web_Audio_API-8a2be2?style=for-the-badge)

---

## ✨ Features

- **Apple Music-Style Frosted Glassmorphism:** Translucent layered glass panels (`backdrop-filter: blur(36px)`), specular glowing borders, and dynamic ambient background lighting that extracts dominant colors from your album cover art.
- **100% Client-Side & Offline (IndexedDB):** Drag-and-drop entire folders or individual songs (`.mp3`, `.flac`, `.wav`, `.m4a`, `.ogg`, `.aac`). Files are stored permanently in your browser's persistent IndexedDB storage—no server, no cloud, no bandwidth, zero subscription.
- **60 FPS Hardware-Accelerated Canvas Visualizer:**
  - *Aurora Neon Bars:* Multi-band EQ frequency spectrum with peak caps.
  - *Liquid Wave:* Fluid oscillating waveform with neon bloom.
  - *Radial Ring:* Pulsating circular audio spectrum reacting to bass kicks.
  - *Stardust Particles:* Cosmic energy particles accelerating to the audio beat.
- **Synced Karaoke Lyrics:** Auto-scrolling, live-synchronized `.lrc` lyrics with active glowing focus line and click-to-seek timestamp jumping.
- **Smart Playback Queue:** Live drag-and-drop / reorderable queue, "Play Next", shuffle with Fisher-Yates, and repeat modes.
- **In-Place ID3 Tag Editor:** Edit Title, Artist, Album, Year, Genre, custom Album Artwork, and paste LRC lyrics on the fly.
- **Native OS Media Integration:** Full MediaSession API integration for Windows lock screen, notification controls, and keyboard media keys.
- **Desktop PWA Support:** Installable directly as a native desktop window via Chrome or Edge.

---

## 🚀 How to Run Locally

Because Aurora is built with modern ES modules and standard Web APIs, it runs locally with zero installation:

1. Open PowerShell in this directory:
   ```powershell
   cd C:\Users\abc\.gemini\antigravity\scratch\aurora-music
   ```

2. Start a local server with Python:
   ```powershell
   python -m http.server 8080
   ```

3. Open your browser to:
   ```text
   http://localhost:8080
   ```

4. Drag and drop any folder of music or individual audio files into the window!

---

## 🌐 How to Deploy on GitHub Pages (Zero Build Step!)

Because Aurora is written natively without heavy compiler dependencies, deploying to GitHub Pages takes less than 60 seconds:

1. Create a new repository on GitHub (e.g. `aurora-music`).
2. Initialize and push this folder:
   ```bash
   git init
   git add .
   git commit -m "Initial release of Aurora Glass Music Player"
   git branch -M main
   git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPO-NAME>.git
   git push -u origin main
   ```
3. In your GitHub repository:
   - Go to **Settings** → **Pages** (on the left sidebar).
   - Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
   - Select Branch: `main`, Folder: `/ (root)`.
   - Click **Save**.
4. Within 1-2 minutes, your player will be live at:
   `https://<YOUR-USERNAME>.github.io/<YOUR-REPO-NAME>/`

---

## ⌨️ Desktop Keyboard Shortcuts

| Key | Action |
| :--- | :--- |
| <kbd>Space</kbd> | Toggle Play / Pause |
| <kbd>←</kbd> | Seek Backward 5 seconds |
| <kbd>→</kbd> | Seek Forward 5 seconds |
| <kbd>↑</kbd> | Volume Up 5% |
| <kbd>↓</kbd> | Volume Down 5% |
| <kbd>M</kbd> | Toggle Mute |
| <kbd>L</kbd> | Toggle Synced Lyrics Drawer |
| <kbd>Q</kbd> | Toggle Smart Queue Drawer |
| <kbd>V</kbd> | Cycle Visualizer Modes |
| <kbd>Esc</kbd> | Exit Stage Mode or Close Modals |
