# Nyx Cortex AI 🧠⚡  
**Enhanced Local AI Assistant for Offensive Security, System Automation, and Real-Time Interaction**

Nyx is an advanced, terminal-based AI assistant designed for ethical hacking, cybersecurity operations, system administration, and task automation. Powered by `llama.cpp` and running a local model (`Nyx_Brain.gguf`), Nyx is fully GPU-accelerated, command-capable, and context-aware.

---

## 🔧 Features

- ✅ **Offline Local AI Model** (no cloud/telemetry)
- 🚀 **GPU Accelerated Inference** with device load balancing
- 🧠 **System-Aware**: Understands CPU, memory, GPU, and OS
- 💻 **Command Execution**: Run `!<shell_command>` directly
- 🔍 **Memory & History Retention**: Remembers past conversations
- 🎛️ **Live Animated Thinking Bar**: Visual feedback while processing
- 🔐 **Cybersecurity Focused Personality**: Red/Blue/Purple team logic baked in
- 🧵 **Loop Detection + Rephrasing**: Avoids repetitive output

---

## 🖥️ Requirements

- Python 3.9+
- CUDA-capable NVIDIA GPUs
- [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python)
- [GPUtil](https://pypi.org/project/GPUtil/)
- Compatible `.gguf` model (e.g., Qwen3 32B Instruct)
- Nyx_Brain.gguf is Unsloth-Qwen3-8B.gguf model (https://huggingface.co/unsloth/Qwen3-8B-GGUF)

### Install Dependencies

```bash
pip install llama-cpp-python GPUtil psutil
```
## 📁 Directory Structure
```bash

Nyx/
├── models/
│   └── Nyx_Brain.gguf         # Your chosen model file
├── nyx_memory.json            # Persistent chat memory
├── Nyx_Cortex.py              # Main AI interface script
```
## 🚀 Usage
Start Nyx:

```bash
python3 Nyx_Cortex.py
```
## In-Terminal Commands
!sysinfo — Show current system CPU, RAM, GPU, and OS info

!<command> — Execute a shell command (e.g., !ls, !neofetch, !uptime)

exit or quit — End the Nyx session

## 💬 Example Interaction
```vbnet
> You: Nyx, scan my local network
Nyx Thinking: ▁▂▃▄▅▆▇█▇▆▅▃▂▁

Nyx: Let’s get started. I'll prepare a Python script using `socket` and `threading` to scan 192.168.1.0/24. Here's the tool...
```
## ⚠️ Disclaimer
Nyx is designed for educational and ethical use only. Do not use this tool or generated content against systems you do not own or lack authorization to test.
## 🧠 Tips
Use lighter models if running on limited VRAM.

You can swap models by replacing Nyx_Brain.gguf with another .gguf file in the models/ folder.

Tune GPU_LAYERS and GPU_SPLIT in the script to optimize for your dual-GPU or single-GPU system.

## 🛡️ Philosophy
"I am Nyx. I assist, I protect, I compute."
Built for red teamers, blue teamers, and curious hackers.
Always local. Always yours. 🖤

# 🛡️ MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**Disclaimer**: The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

# 🛡️ Disclaimer

ShadowDrums and ShadowTEAM members will not be held liable for any misuse of this source code, program, or software. It is the responsibility of the user to ensure that their use of this software complies with all applicable laws and regulations. By using this software, you agree to indemnify and hold harmless Shadowdrums and ShadowTEAM members from any claims, damages, or liabilities arising from your use or misuse of the software.

---

## 🤝 Credits
- Qwen3 8B model
- Built with love for real operators. Stay sharp. 🛡️
- Shadowdrums
