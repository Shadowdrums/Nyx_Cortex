#!/usr/bin/env python3
# Nyx_Cortex.py — Enhanced Single-Model AI Brain (Nyx_Brain.gguf only, GPU optimized with load balancing, animated, system aware, command execution)

import os, sys, time, json, threading, psutil, subprocess, platform, GPUtil
import math
import itertools, random
from llama_cpp import Llama, llama_print_system_info
from pathlib import Path

# === CONFIG ===
MODEL_DIR = Path("~/2025-projects/Nyx/models").expanduser()
MEMORY_FILE = Path("~/2025-projects/Nyx/nyx_memory.json").expanduser()
MAX_TOKENS = 4096
CONTEXT_WINDOW = 8192
GPU_LAYERS = 49  # Match full model depth
MAIN_GPU_INDEX = 0
GPU_SPLIT = [0.5, 0.5]  # Distribute across two GPUs evenly
MODEL_PATH = MODEL_DIR / "Nyx_Brain.gguf"

# === UTILITY ===
def load_memory():
    if MEMORY_FILE.exists():
        try:
            return json.loads(MEMORY_FILE.read_text())
        except json.JSONDecodeError:
            print("[!] Corrupt memory file. Starting fresh.")
    return {"history": [], "sysinfo": {}}

def save_memory(mem):
    MEMORY_FILE.write_text(json.dumps(mem, indent=2))

# === LOAD MODEL ===
if not MODEL_PATH.exists():
    print(f"[!] Model not found at: {MODEL_PATH}")
    sys.exit(1)

print(f"[+] Loading Nyx Brain model with GPU acceleration: {MODEL_PATH.name}")
print("[+] LLaMA System Info:\n")
print(llama_print_system_info().decode())

llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=CONTEXT_WINDOW,
    n_gpu_layers=GPU_LAYERS,
    use_gpu=True,
    n_threads=os.cpu_count(),
    main_gpu=MAIN_GPU_INDEX,
    tensor_split=GPU_SPLIT
)

# === ANIMATED THINKING (WAVEFORM) ===
def animate_thinking(stop_event):
    prefix = "\033[1;95mNyx Thinking:\033[0m "
    blocks = "▁▂▃▄▅▆▇█"  # 8 heights
    width = 30
    tail = ['▁'] * width

    sys.stdout.write(prefix)
    sys.stdout.flush()

    while not stop_event.is_set():
        new_height = random.choices(range(len(blocks)), weights=[3, 5, 7, 10, 7, 5, 3, 2])[0]
        new_block = blocks[new_height]
        if random.random() < 0.05:
            new_block = '▁'
        tail.pop(0)
        tail.append(new_block)
        waveform = ''.join(f"\033[95m{c}\033[0m" for c in tail)

        sys.stdout.write('\r' + ' ' * (len(prefix) + width) + '\r')
        sys.stdout.write(prefix + waveform)
        sys.stdout.flush()
        time.sleep(0.07)

    sys.stdout.write('\r' + ' ' * (len(prefix) + width) + '\r')
    sys.stdout.flush()

# === SYSTEM AWARENESS ===
def system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    gpu_info_list = GPUtil.getGPUs()
    gpu_info = " | ".join([f"{gpu.name} {gpu.load * 100:.1f}% ({gpu.temperature}°C)" for gpu in gpu_info_list]) or "No GPU detected"
    os_info = f"{platform.system()} {platform.release()} ({platform.version()})"
    return f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory.percent}%\nGPU Info: {gpu_info}\nOS: {os_info}"

# === COMMAND EXECUTION ===
def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

# === PROMPT BUILDER ===
def build_prompt(user_input, memory):
    history = memory.get("history", [])[-6:]
    context = "\n".join([f"User: {h['user']}\nNyx: {h['nyx']}" for h in history])
    sysinfo = memory.get("sysinfo", "")
    thoughts = f"[Nyx Internal Thought Process]\n- Recalling system status and recent context...\n- Interpreting user intent...\n- Formulating response based on cybersecurity-focused reasoning.\n- Checking for potential command execution paths...\n"
    print(f"\n\033[94m{thoughts}\033[0m")
    return f"""
You are Nyx, an advanced AI assistant running on a secure, privileged local system. You specialize in cybersecurity, red team, blue team, and purple team operations. You **can** execute shell commands, access system information, modify files, and perform tasks if the user requests them explicitly. You do **not** refuse actions unless they pose a risk or are clearly unauthorized. Be helpful, efficient, and clear in your output.

System Information:
{sysinfo}

{context}

User: {user_input}
Nyx:"""

# === INTERACTION LOOP ===
def interact():
    memory = load_memory()
    memory["sysinfo"] = system_info()
    save_memory(memory)

    print("\n[Type 'exit' or 'quit' to end the session. Commands: '!sysinfo', '!<command>' to execute commands directly]")
    last_response = ""
    while True:
        try:
            user_input = input("\n> You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("Nyx: Goodbye. Stay secure.")
                break

            if user_input.lower() == "!sysinfo":
                info = system_info()
                memory["sysinfo"] = info
                save_memory(memory)
                print(info)
                continue

            if user_input.startswith("!"):
                command = user_input[1:]
                command_output = execute_command(command)
                print(f"\n\033[92m[+] Nyx executed:\033[0m `{command}`\n{command_output.strip()}\n")
                continue

            thinking_event = threading.Event()
            threading.Thread(target=animate_thinking, args=(thinking_event,), daemon=True).start()

            prompt = build_prompt(user_input, memory)
            response = llm(prompt, max_tokens=MAX_TOKENS, stop=["User:"], echo=False)

            thinking_event.set()

            nyx_raw = response["choices"][0]["text"].strip()
            for tag in ["<thinking>", "</thinking>", "<unk>"]:
                nyx_raw = nyx_raw.replace(tag, "")

            # Prevent repeating previous response
            if nyx_raw == last_response:
                print("\n\033[91m[!] Loop detected. Rephrasing...\033[0m")
                prompt += "\n(Do not repeat yourself. Rephrase your answer.)"
                response = llm(prompt, max_tokens=MAX_TOKENS, stop=["User:"], echo=False)
                nyx_raw = response["choices"][0]["text"].strip()
                for tag in ["<thinking>", "</thinking>", "<unk>"]:
                    nyx_raw = nyx_raw.replace(tag, "")

            last_response = nyx_raw

            for char in nyx_raw:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.005)

            memory["history"].append({"user": user_input, "nyx": nyx_raw})
            save_memory(memory)

        except KeyboardInterrupt:
            print("\n[!] Session interrupted.")
            break

if __name__ == "__main__":
    print("\n>> NYX vCORTEX — ENHANCED SINGLE MODEL ONLINE <<")
    interact()
