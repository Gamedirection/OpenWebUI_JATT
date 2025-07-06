#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

class OpenWebUIConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Open WebUI Chat Exporter")
        self.root.geometry("500x300")
        
        # GUI Elements
        self.setup_gui()
        
    def setup_gui(self):
        """Create and arrange GUI components"""
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Title
        tk.Label(
            main_frame, 
            text="Open WebUI Chat Export Converter",
            font=("Arial", 16, "bold")
        ).pack(pady=(0, 20))
        
        # File selection button
        tk.Button(
            main_frame,
            text="Select JSON Export File",
            command=self.select_file,
            height=2,
            width=25
        ).pack(pady=10)
        
        # Output directory selection
        self.output_var = tk.StringVar(value="converted_chats")
        tk.Label(main_frame, text="Output Directory:").pack()
        output_frame = tk.Frame(main_frame)
        output_frame.pack()
        tk.Entry(output_frame, textvariable=self.output_var, width=30).pack(side=tk.LEFT, padx=5)
        tk.Button(
            output_frame,
            text="Browse",
            command=self.select_output_dir
        ).pack(side=tk.LEFT)
        
        # Convert button
        tk.Button(
            main_frame,
            text="Convert to TXT",
            command=self.start_conversion,
            height=2,
            width=25,
            bg="#4CAF50",
            fg="white"
        ).pack(pady=20)
        
        # Status label
        self.status_var = tk.StringVar()
        tk.Label(main_frame, textvariable=self.status_var, fg="blue").pack()
        
    def select_file(self):
        """Open file dialog to select JSON file"""
        file_path = filedialog.askopenfilename(
            title="Select Open WebUI JSON Export",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            self.input_file = file_path
            self.status_var.set(f"Selected: {os.path.basename(file_path)}")
    
    def select_output_dir(self):
        """Open dialog to select output directory"""
        dir_path = filedialog.askdirectory(
            title="Select Output Folder",
            mustexist=True
        )
        if dir_path:
            self.output_var.set(dir_path)
    
    def validate_json(self, filepath):
        """Verify JSON file is valid"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                json.load(f)
            return True
        except json.JSONDecodeError as e:
            messagebox.showerror("JSON Error", f"Invalid JSON file:\n{str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file:\n{str(e)}")
        return False
    
    def convert_conversation(self, conv, output_dir):
        """Convert a single conversation to TXT"""
        try:
            chat_data = conv.get('chat', {})
            title = chat_data.get('title') or conv.get('title', 'Untitled')
            messages = []
            
            # Collect messages from all possible locations
            if 'messages' in chat_data:
                messages.extend(chat_data['messages'])
            if 'history' in chat_data and 'messages' in chat_data['history']:
                messages.extend(chat_data['history']['messages'].values())
            
            if not messages:
                return False
            
            # Create safe filename
            safe_title = "".join(c if c.isalnum() or c in ' ._-' else '_' for c in str(title))
            filename = f"{output_dir}/{safe_title[:100]}.txt"
            
            # Write conversation to file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"=== {title} ===\n\n")
                
                for msg in messages:
                    content = msg.get('content', '')
                    if not str(content).strip():
                        continue
                    
                    role = msg.get('role', 'unknown').capitalize()
                    if role.lower() == 'assistant':
                        role = 'AI'
                    elif role.lower() == 'user':
                        role = 'You'
                    
                    # Format timestamp
                    timestamp = ""
                    if 'timestamp' in msg:
                        try:
                            ts = msg['timestamp']
                            if len(str(ts)) == 10:  # Unix timestamp
                                dt = datetime.fromtimestamp(ts)
                            else:  # Possibly milliseconds
                                dt = datetime.fromtimestamp(ts/1000)
                            timestamp = dt.strftime("[%Y-%m-%d %H:%M:%S] ")
                        except:
                            pass
                    
                    f.write(f"{timestamp}{role}: {content}\n\n")
                
                f.write("="*60 + "\n")
            
            return True
        
        except Exception as e:
            print(f"Error converting conversation: {str(e)}")
            return False
    
    def start_conversion(self):
        """Main conversion function triggered by GUI"""
        if not hasattr(self, 'input_file'):
            messagebox.showwarning("No File", "Please select a JSON file first")
            return
        
        if not self.validate_json(self.input_file):
            return
        
        output_dir = self.output_var.get()
        Path(output_dir).mkdir(exist_ok=True)
        
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Process conversations
            conversations = data if isinstance(data, list) else [data]
            success_count = 0
            
            self.status_var.set("Converting...")
            self.root.update()
            
            for conv in conversations:
                if self.convert_conversation(conv, output_dir):
                    success_count += 1
            
            messagebox.showinfo(
                "Conversion Complete",
                f"Successfully converted {success_count} conversations\n"
                f"Output directory: {os.path.abspath(output_dir)}"
            )
            self.status_var.set(f"Converted {success_count} conversations")
            
        except Exception as e:
            messagebox.showerror(
                "Conversion Error",
                f"Failed during conversion:\n{str(e)}"
            )
            self.status_var.set("Conversion failed")

    def run(self):
        """Run the application"""
        self.root.mainloop()

if __name__ == "__main__":
    converter = OpenWebUIConverter()
    converter.run()
