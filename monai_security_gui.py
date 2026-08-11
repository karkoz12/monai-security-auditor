"""
monai_security_gui.py

Simple GUI wrapper for MONAI Security security.

Place this file in the same folder as monai_security.py, then run:

    python monai_security_gui.py

Features:
- Browse project folder
- Browse dataset folder
- Browse model file/folder
- Browse output folder
- Run security assessment
- Show console log
- Open PDF / HTML / Radiologist View / Developer View / output folder

This GUI is a thin layer over the same MONAI Security engine.
"""

from __future__ import annotations

import os
import sys
import json
import queue
import threading
import subprocess
import webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


APP_TITLE = "MONAI Security - AI Model Safety Check"


def safe_path(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


class MonaiSecurityGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.minsize(1050, 720)

        self.process = None
        self.log_queue = queue.Queue()
        self.last_output_dir = None

        self.project_var = tk.StringVar(value=str(Path.cwd()))
        self.dataset_var = tk.StringVar(value="")
        self.model_var = tk.StringVar(value="")
        self.output_var = tk.StringVar(value=str(Path.cwd() / "monai_security_report"))
        self.status_var = tk.StringVar(value="Ready")
        self.score_var = tk.StringVar(value="-")
        self.security_status_var = tk.StringVar(value="-")
        self.action_var = tk.StringVar(value="-")

        self._setup_style()
        self._build_ui()
        self._poll_log_queue()

    # -----------------------------------------------------
    # UI setup
    # -----------------------------------------------------
    def _setup_style(self):
        style = ttk.Style(self.root)
        try:
            style.theme_use("clam")
        except Exception:
            pass

        bg = "#0f172a"
        panel = "#111827"
        card = "#1f2937"
        fg = "#e5e7eb"
        accent = "#38bdf8"

        self.root.configure(bg=bg)

        style.configure(".", background=bg, foreground=fg, fieldbackground=card)
        style.configure("TFrame", background=bg)
        style.configure("Card.TFrame", background=panel)
        style.configure("TLabel", background=bg, foreground=fg)
        style.configure("Card.TLabel", background=panel, foreground=fg)
        style.configure("Title.TLabel", background=bg, foreground=fg, font=("Segoe UI", 18, "bold"))
        style.configure("Header.TLabel", background=panel, foreground=fg, font=("Segoe UI", 12, "bold"))
        style.configure("Score.TLabel", background=panel, foreground=accent, font=("Segoe UI", 34, "bold"))
        style.configure("TButton", padding=6)
        style.configure("Accent.TButton", padding=8, font=("Segoe UI", 10, "bold"))
        style.configure("TEntry", fieldbackground="#ffffff", foreground="#111827")

    def _build_ui(self):
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)

        title = ttk.Label(self.root, text="MONAI Security - AI Model Safety Check", style="Title.TLabel")
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=18, pady=(16, 10))

        left = ttk.Frame(self.root, style="Card.TFrame", padding=14)
        left.grid(row=1, column=0, sticky="nsw", padx=(18, 8), pady=(0, 18))
        left.columnconfigure(1, weight=1)

        right = ttk.Frame(self.root, padding=0)
        right.grid(row=1, column=1, sticky="nsew", padx=(8, 18), pady=(0, 18))
        right.columnconfigure(0, weight=1)
        right.rowconfigure(2, weight=1)

        self._build_input_panel(left)
        self._build_dashboard(right)
        self._build_log_panel(right)
        self._build_report_buttons(right)

    def _build_input_panel(self, parent):
        row = 0
        ttk.Label(parent, text="Security assessment setup", style="Header.TLabel").grid(row=row, column=0, columnspan=3, sticky="w", pady=(0, 12))
        row += 1

        self._path_row(parent, row, "Project", self.project_var, self.pick_project)
        row += 1

        self._path_row(parent, row, "Dataset", self.dataset_var, self.pick_dataset)
        row += 1

        self._path_row(parent, row, "Model", self.model_var, self.pick_model, file_or_folder=True)
        row += 1

        self._path_row(parent, row, "Output", self.output_var, self.pick_output)
        row += 1

        ttk.Separator(parent).grid(row=row, column=0, columnspan=3, sticky="ew", pady=12)
        row += 1

        ttk.Button(parent, text="Auto-detect dataset/model", command=self.auto_detect).grid(row=row, column=0, columnspan=3, sticky="ew", pady=(0, 8))
        row += 1

        ttk.Button(parent, text="Run MONAI Security Assessment", style="Accent.TButton", command=self.run_security).grid(row=row, column=0, columnspan=3, sticky="ew", pady=(0, 8))
        row += 1

        ttk.Button(parent, text="Stop", command=self.stop_security).grid(row=row, column=0, columnspan=3, sticky="ew")
        row += 1

        ttk.Separator(parent).grid(row=row, column=0, columnspan=3, sticky="ew", pady=12)
        row += 1

        ttk.Label(parent, text="Demo shortcuts", style="Header.TLabel").grid(row=row, column=0, columnspan=3, sticky="w", pady=(0, 8))
        row += 1

        ttk.Button(parent, text="Load PASS demo folder", command=self.pick_pass_demo).grid(row=row, column=0, columnspan=3, sticky="ew", pady=(0, 6))
        row += 1

        ttk.Button(parent, text="Load ISSUE demo folder", command=self.pick_issue_demo).grid(row=row, column=0, columnspan=3, sticky="ew")
        row += 1

        ttk.Separator(parent).grid(row=row, column=0, columnspan=3, sticky="ew", pady=12)
        row += 1

        ttk.Label(parent, textvariable=self.status_var, style="Card.TLabel", wraplength=330).grid(row=row, column=0, columnspan=3, sticky="ew")

    def _path_row(self, parent, row, label, var, command, file_or_folder=False):
        ttk.Label(parent, text=label, style="Card.TLabel").grid(row=row, column=0, sticky="w", pady=4)
        entry = ttk.Entry(parent, textvariable=var, width=38)
        entry.grid(row=row, column=1, sticky="ew", padx=6, pady=4)
        ttk.Button(parent, text="Browse", command=command).grid(row=row, column=2, sticky="e", pady=4)

    def _build_dashboard(self, parent):
        card = ttk.Frame(parent, style="Card.TFrame", padding=14)
        card.grid(row=0, column=0, sticky="ew")
        card.columnconfigure(0, weight=0)
        card.columnconfigure(1, weight=1)

        ttk.Label(card, text="Model Safety Score", style="Header.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(card, textvariable=self.score_var, style="Score.TLabel").grid(row=1, column=0, sticky="w", padx=(0, 30))

        ttk.Label(card, text="Status", style="Header.TLabel").grid(row=0, column=1, sticky="w")
        ttk.Label(card, textvariable=self.security_status_var, style="Card.TLabel", font=("Segoe UI", 15, "bold")).grid(row=1, column=1, sticky="w")
        ttk.Label(card, text="Recommended action", style="Header.TLabel").grid(row=2, column=1, sticky="w", pady=(14, 0))
        ttk.Label(card, textvariable=self.action_var, style="Card.TLabel", wraplength=650).grid(row=3, column=1, sticky="w")

    def _build_log_panel(self, parent):
        log_frame = ttk.Frame(parent, style="Card.TFrame", padding=10)
        log_frame.grid(row=2, column=0, sticky="nsew", pady=(12, 0))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(1, weight=1)

        ttk.Label(log_frame, text="Security log", style="Header.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 8))

        self.log_text = tk.Text(
            log_frame,
            height=22,
            bg="#020617",
            fg="#e5e7eb",
            insertbackground="#e5e7eb",
            relief="flat",
            wrap="word",
            font=("Consolas", 10),
        )
        self.log_text.grid(row=1, column=0, sticky="nsew")

        scroll = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        scroll.grid(row=1, column=1, sticky="ns")
        self.log_text.configure(yscrollcommand=scroll.set)

    def _build_report_buttons(self, parent):
        frame = ttk.Frame(parent, style="Card.TFrame", padding=10)
        frame.grid(row=3, column=0, sticky="ew", pady=(12, 0))

        ttk.Button(frame, text="Open PDF", command=self.open_pdf).grid(row=0, column=0, padx=4)
        ttk.Button(frame, text="Open HTML", command=self.open_html).grid(row=0, column=1, padx=4)
        ttk.Button(frame, text="Radiologist View", command=self.open_radiologist).grid(row=0, column=2, padx=4)
        ttk.Button(frame, text="Developer View", command=self.open_developer).grid(row=0, column=3, padx=4)
        ttk.Button(frame, text="Open Output Folder", command=self.open_output_folder).grid(row=0, column=4, padx=4)

    # -----------------------------------------------------
    # Pickers
    # -----------------------------------------------------
    def pick_project(self):
        path = filedialog.askdirectory(title="Select MONAI project folder")
        if path:
            self.project_var.set(path)
            self.output_var.set(str(Path(path).resolve() / "monai_security_report"))
            self.auto_detect()

    def pick_dataset(self):
        path = filedialog.askdirectory(title="Select dataset folder")
        if path:
            self.dataset_var.set(path)

    def pick_model(self):
        path = filedialog.askopenfilename(
            title="Select model file, or cancel and choose folder in next dialog",
            filetypes=[
                ("Model files", "*.pt *.pth *.ckpt *.onnx *.ts *.torchscript *.safetensors"),
                ("All files", "*.*"),
            ],
        )
        if path:
            self.model_var.set(path)
            return

        folder = filedialog.askdirectory(title="Select model folder")
        if folder:
            self.model_var.set(folder)

    def pick_output(self):
        path = filedialog.askdirectory(title="Select output folder")
        if path:
            self.output_var.set(path)

    def pick_pass_demo(self):
        path = filedialog.askdirectory(title="Select one PASS demo project folder")
        if path:
            self.project_var.set(path)
            self.dataset_var.set(str(Path(path) / "data"))
            self.model_var.set(str(Path(path) / "models"))
            self.output_var.set(str(Path(path) / "security_output"))

    def pick_issue_demo(self):
        path = filedialog.askdirectory(title="Select one ISSUE demo project folder")
        if path:
            self.project_var.set(path)
            self.dataset_var.set(str(Path(path) / "data"))
            self.model_var.set(str(Path(path) / "models"))
            self.output_var.set(str(Path(path) / "security_output"))

    # -----------------------------------------------------
    # Detection and security
    # -----------------------------------------------------
    def auto_detect(self):
        project = Path(self.project_var.get()).resolve()

        for name in ("data", "dataset", "datasets", "images"):
            candidate = project / name
            if candidate.exists() and candidate.is_dir():
                self.dataset_var.set(str(candidate))
                break

        model_candidates = []
        for ext in ("*.safetensors", "*.onnx", "*.pt", "*.pth", "*.ckpt", "*.ts", "*.torchscript"):
            model_candidates.extend(project.rglob(ext))

        model_candidates = [p for p in model_candidates if "monai_security_report" not in p.parts and "security_output" not in p.parts]
        if model_candidates:
            self.model_var.set(str(model_candidates[0].parent))
        elif (project / "models").exists():
            self.model_var.set(str(project / "models"))

        self.append_log("Auto-detection finished.")

    def run_security(self):
        if self.process is not None:
            messagebox.showwarning("Security assessment running", "A security assessment is already running.")
            return

        project = self.project_var.get().strip()
        dataset = self.dataset_var.get().strip()
        model = self.model_var.get().strip()
        output = self.output_var.get().strip()

        if not project or not Path(project).exists():
            messagebox.showerror("Missing project", "Select a valid project folder.")
            return

        security_py = Path(__file__).parent / "monai_security.py"
        if not security_py.exists():
            messagebox.showerror("Missing monai_security.py", "monai_security.py must be in the same folder as monai_security_gui.py.")
            return

        cmd = [sys.executable, str(security_py), "security", project, "--out", output]

        if dataset:
            cmd.extend(["--dataset", dataset])
        if model:
            cmd.extend(["--model", model])

        self.last_output_dir = Path(output)
        self.clear_log()
        self.reset_dashboard()
        self.status_var.set("Running security assessment...")
        self.append_log("Command:")
        self.append_log(" ".join(f'"{x}"' if " " in x else x for x in cmd))
        self.append_log("")

        thread = threading.Thread(target=self._run_process, args=(cmd,), daemon=True)
        thread.start()

    def _run_process(self, cmd):
        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True,
            )

            assert self.process.stdout is not None
            for line in self.process.stdout:
                self.log_queue.put(line.rstrip())

            code = self.process.wait()
            self.log_queue.put(f"\nProcess finished with code {code}")
            self.log_queue.put("__AUDIT_DONE__")

        except Exception as e:
            self.log_queue.put(f"ERROR: {e}")
            self.log_queue.put("__AUDIT_DONE__")
        finally:
            self.process = None

    def stop_security(self):
        if self.process is not None:
            self.process.terminate()
            self.append_log("Stopping security...")
            self.status_var.set("Stopping security.")

    # -----------------------------------------------------
    # Dashboard parsing
    # -----------------------------------------------------
    def load_summary_from_json(self):
        if not self.last_output_dir:
            return

        candidates = [
            self.last_output_dir / "monai_security_report.json",
            self.last_output_dir / "security_report.json",
            self.last_output_dir / "json" / "security_report.json",
            self.last_output_dir / "json" / "monai_security_report.json",
            self.last_output_dir / "json" / "monoai_audit_report.json",
        ]

        report = None
        for c in candidates:
            if c.exists():
                report = c
                break

        if report is None:
            self.status_var.set("Security assessment finished, but no JSON report was found.")
            return

        try:
            payload = json.loads(report.read_text(encoding="utf-8"))
            risk = payload.get("risk_score") or payload.get("risk_summary")

            if risk:
                score = risk.get("score", "-")
                status = risk.get("status", "-")
                action = risk.get("recommended_action", "-")
                self.score_var.set(f"{score}/100")
                self.security_status_var.set(status)
                self.action_var.set(action)
                self.status_var.set("Security assessment finished.")
            else:
                issues = payload.get("issues", [])
                self.score_var.set("N/A")
                self.security_status_var.set(f"Security report generated: {len(issues)} issue(s)")
                self.action_var.set("Open the HTML or PDF report for full findings.")
                self.status_var.set("Security assessment finished.")
        except Exception as e:
            self.status_var.set(f"Could not read report: {e}")

    def reset_dashboard(self):
        self.score_var.set("-")
        self.security_status_var.set("-")
        self.action_var.set("-")

    # -----------------------------------------------------
    # Log
    # -----------------------------------------------------
    def append_log(self, text):
        self.log_text.insert("end", text + "\n")
        self.log_text.see("end")

    def clear_log(self):
        self.log_text.delete("1.0", "end")

    def _poll_log_queue(self):
        try:
            while True:
                item = self.log_queue.get_nowait()
                if item == "__AUDIT_DONE__":
                    self.load_summary_from_json()
                else:
                    self.append_log(item)
        except queue.Empty:
            pass

        self.root.after(150, self._poll_log_queue)

    # -----------------------------------------------------
    # Open reports
    # -----------------------------------------------------
    def _open_file(self, path: Path):
        if not path.exists():
            messagebox.showwarning("Missing file", f"File not found:\n{path}")
            return
        try:
            if sys.platform.startswith("win"):
                os.startfile(str(path))
            else:
                webbrowser.open(path.as_uri())
        except Exception as e:
            messagebox.showerror("Open error", str(e))

    def open_pdf(self):
        out = Path(self.output_var.get())
        for candidate in [
            out / "monai_security_report.pdf",
            out / "security_report.pdf",
            out / "reports" / "security_report.pdf",
        ]:
            if candidate.exists():
                self._open_file(candidate)
                return
        self._open_file(out / "monai_security_report.pdf")

    def open_html(self):
        out = Path(self.output_var.get())
        for candidate in [
            out / "monai_security_report.html",
            out / "security_report.html",
            out / "reports" / "security_report.html",
        ]:
            if candidate.exists():
                self._open_file(candidate)
                return
        self._open_file(out / "monai_security_report.html")

    def open_radiologist(self):
        out = Path(self.output_var.get())
        for candidate in [
            out / "radiologist_view.html",
            out / "reports" / "radiologist_view.html",
            out / "monai_security_report.html",
        ]:
            if candidate.exists():
                self._open_file(candidate)
                return
        self._open_file(out / "monai_security_report.html")

    def open_developer(self):
        out = Path(self.output_var.get())
        for candidate in [
            out / "developer_view.html",
            out / "reports" / "developer_view.html",
            out / "monai_security_report.md",
            out / "monai_security_report.html",
        ]:
            if candidate.exists():
                self._open_file(candidate)
                return
        self._open_file(out / "monai_security_report.md")

    def open_output_folder(self):
        out = Path(self.output_var.get())
        if not out.exists():
            messagebox.showwarning("Missing folder", f"Folder not found:\n{out}")
            return
        try:
            if sys.platform.startswith("win"):
                os.startfile(str(out))
            else:
                webbrowser.open(out.as_uri())
        except Exception as e:
            messagebox.showerror("Open error", str(e))


def main():
    root = tk.Tk()
    app = MonaiSecurityGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
