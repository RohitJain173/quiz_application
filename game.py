import tkinter as tk
from tkinter import messagebox, ttk
import os

questions_bank = {
    "General Knowledge": {
        "Easy": [
            {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Bangalore", "Hyderabad"], "answer": 1},
            {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": 2},
            {"question": "Which planet is closest to the sun?", "options": ["Mars", "Mercury", "Venus", "Earth"], "answer": 1},
            {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": 2},
            {"question": "What is the national flower of India?", "options": ["Rose", "Lotus", "Marigold", "Lily"], "answer": 1}
        ],
        "Medium": [
            {"question": "Who wrote the National Anthem of India?", "options": ["Bankim Chandra", "Rabindranath Tagore", "Mahatma Gandhi", "Bal Gangadhar Tilak"], "answer": 1},
            {"question": "Which year did India gain independence?", "options": ["1947", "1950", "1942", "1930"], "answer": 0},
            {"question": "Who is known as the Father of the Nation?", "options": ["Jawaharlal Nehru", "Subhas Chandra Bose", "Mahatma Gandhi", "Sardar Patel"], "answer": 2},
            {"question": "Where is the Gateway of India located?", "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"], "answer": 1},
            {"question": "Which is the longest river in India?", "options": ["Yamuna", "Ganga", "Godavari", "Brahmaputra"], "answer": 1}
        ],
        "Hard": [
            {"question": "Who was the first President of India?", "options": ["Jawaharlal Nehru", "Rajendra Prasad", "S. Radhakrishnan", "APJ Abdul Kalam"], "answer": 1},
            {"question": "What is the national aquatic animal of India?", "options": ["Dolphin", "Shark", "Crocodile", "Fish"], "answer": 0},
            {"question": "Which city is known as the Silicon Valley of India?", "options": ["Hyderabad", "Pune", "Bangalore", "Mumbai"], "answer": 2},
            {"question": "In which year did the Jallianwala Bagh massacre occur?", "options": ["1919", "1920", "1931", "1942"], "answer": 0},
            {"question": "What is the name of India's first satellite?", "options": ["Aryabhata", "INSAT", "Bhaskara", "Rohini"], "answer": 0}
        ]
    },
    "Technology": {
        "Easy": [
            {"question": "Which programming language is used for AI?", "options": ["Python", "HTML", "CSS", "SQL"], "answer": 0},
            {"question": "HTML stands for?", "options": ["Hyper Text", "Hyperlink Markup", "HighText Machine", "HyperText Markup Language"], "answer": 3},
            {"question": "What does CPU stand for?", "options": ["Central Processing Unit", "Control Processing Unit", "Central Print Unit", "Computer Processing Unit"], "answer": 0},
            {"question": "What is the full form of USB?", "options": ["Universal Serial Bus", "United System Base", "User Selective Bus", "Universal System Board"], "answer": 0},
            {"question": "Which one is a search engine?", "options": ["Chrome", "Windows", "Google", "Facebook"], "answer": 2}
        ],
        "Medium": [
            {"question": "What does RAM stand for?", "options": ["Read Access Memory", "Random Access Memory", "Run All Memory", "Randomly Allocated Memory"], "answer": 1},
            {"question": "Which company developed the Windows OS?", "options": ["Apple", "Microsoft", "IBM", "Google"], "answer": 1},
            {"question": "Who is the founder of Facebook?", "options": ["Elon Musk", "Steve Jobs", "Larry Page", "Mark Zuckerberg"], "answer": 3},
            {"question": "What does URL stand for?", "options": ["Uniform Resource Locator", "Universal Resource Link", "United Routing Language", "Unidentified Reference Location"], "answer": 0},
            {"question": "Which device is used to input data?", "options": ["Monitor", "Keyboard", "Printer", "Speaker"], "answer": 1}
        ],
        "Hard": [
            {"question": "Which language is used to develop Android apps?", "options": ["Python", "Java", "C#", "Ruby"], "answer": 1},
            {"question": "Who is the founder of Microsoft?", "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Larry Page"], "answer": 1},
            {"question": "What is the shortcut for paste?", "options": ["Ctrl + P", "Ctrl + C", "Ctrl + X", "Ctrl + V"], "answer": 3},
            {"question": "What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "HyperText Transfer Package", "High Transfer Text Protocol", "HyperText Tool Protocol"], "answer": 0},
            {"question": "Which is not a programming language?", "options": ["Python", "Java", "HTML", "MySQL"], "answer": 3}
        ]
    }
}

class StylishQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Quiz Game ✨")
        self.root.geometry("950x650")
        self.root.configure(bg="#f4f6f7")

        self.username = ""
        self.category = ""
        self.level = ""
        self.score = 0
        self.q_index = 0
        self.user_answers = []
        self.timer_seconds = 15
        self.timer_id = None
        self.questions = []

        self.setup_styles()
        self.welcome_screen()

    def setup_styles(self):
        self.title_font = ("Verdana", 26, "bold")
        self.label_font = ("Calibri", 16)
        self.question_font = ("Segoe UI", 20, "bold")
        self.option_font = ("Calibri", 15)
        self.button_font = ("Calibri", 14, "bold")

    def welcome_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="🎓Quiz Game", font=self.title_font, bg="#f4f6f7", fg="#2c3e50").pack(pady=40)

        tk.Label(self.root, text="Enter your name:", font=self.label_font, bg="#f4f6f7").pack()
        self.name_entry = tk.Entry(self.root, font=self.label_font, width=30)
        self.name_entry.pack(pady=10)

        tk.Label(self.root, text="Select Category:", font=self.label_font, bg="#f4f6f7").pack(pady=5)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(self.root, textvariable=self.category_var, values=list(questions_bank.keys()), font=self.label_font, state="readonly", width=30)
        self.category_combo.pack()

        tk.Label(self.root, text="Select Level:", font=self.label_font, bg="#f4f6f7").pack(pady=5)
        self.level_var = tk.StringVar()
        self.level_combo = ttk.Combobox(self.root, textvariable=self.level_var, values=["Easy", "Medium", "Hard"], font=self.label_font, state="readonly", width=30)
        self.level_combo.pack()

        tk.Button(self.root, text="🚀 Start Quiz", font=self.button_font, bg="#28a745", fg="white", command=self.start_quiz).pack(pady=30)

    def start_quiz(self):
        self.username = self.name_entry.get().strip()
        self.category = self.category_var.get()
        self.level = self.level_var.get()
        if not self.username or not self.category or not self.level:
            return messagebox.showwarning("Input Error", "Please fill all the fields.")
        self.questions = questions_bank[self.category][self.level]
        self.q_index = 0
        self.score = 0
        self.user_answers = []
        self.quiz_screen()

    def quiz_screen(self):
        self.clear_screen()
        self.var = tk.IntVar(value=-1)
        tk.Label(self.root, text=f"👤 {self.username} | 📚 {self.category} - {self.level}", font=self.label_font, bg="#f4f6f7", fg="#34495e").pack(anchor="ne", padx=20)
        self.timer_label = tk.Label(self.root, font=self.label_font, fg="#e74c3c", bg="#f4f6f7")
        self.timer_label.pack(anchor="ne", padx=20)

        self.question_label = tk.Label(self.root, wraplength=750, font=self.question_font, bg="#f4f6f7")
        self.question_label.pack(pady=40)

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, variable=self.var, value=i, font=self.option_font, bg="#f4f6f7", anchor="w", cursor="hand2", padx=20)
            rb.pack(anchor="w", padx=120, pady=5)
            self.option_buttons.append(rb)

        tk.Button(self.root, text="Next ➡️", font=self.button_font, bg="#007bff", fg="white", command=self.next_question).pack(pady=30)

        self.load_question()
        self.start_timer()

    def load_question(self):
        q = self.questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}: {q['question']}")
        for i, opt in enumerate(q["options"]):
            self.option_buttons[i].config(text=opt)

    def start_timer(self):
        self.timer_seconds = 15
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"⏱ Time Left: {self.timer_seconds} sec")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("⏰ Time's Up!", "Moving to next question...")
            self.next_question()

    def next_question(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        selected = self.var.get()
        self.user_answers.append(selected)
        if selected == self.questions[self.q_index]["answer"]:
            self.score += 1
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.quiz_screen()
        else:
            self.show_result()

    def save_to_leaderboard(self):
        entry = f"{self.username},{self.score},{self.category},{self.level}\n"
        with open("leaderboard.txt", "a") as f:
            f.write(entry)

    def get_leaderboard(self):
        try:
            with open("leaderboard.txt", "r") as f:
                entries = f.readlines()
            leaderboard = []
            for e in entries:
                name, score, cat, lvl = e.strip().split(",")
                leaderboard.append({"name": name, "score": int(score), "category": cat, "level": lvl})
            leaderboard.sort(key=lambda x: x["score"], reverse=True)
            return leaderboard[:5]
        except FileNotFoundError:
            return []

    def show_result(self):
        self.save_to_leaderboard()
        self.clear_screen()
        total = len(self.questions)
        percentage = int((self.score / total) * 100)
        remark = "🎉 Excellent!" if percentage >= 80 else "🙂 Good Job!" if percentage >= 60 else "😐 Can Do Better!" if percentage >= 40 else "😢 Try Again!"

        tk.Label(self.root, text=f"{remark}", font=self.title_font, bg="#f4f6f7", fg="#27ae60").pack(pady=30)
        tk.Label(self.root, text=f"{self.username}'s Score: {self.score} / {total} ({percentage}%)", font=self.label_font, bg="#f4f6f7").pack()

        frame = tk.Frame(self.root, bg="#f4f6f7"); frame.pack(pady=20)
        for i, q in enumerate(self.questions):
            correct = q['answer']
            user = self.user_answers[i]
            status = "❌ Not Attempted" if user == -1 else ("✅ Correct" if user == correct else f"❌ Wrong (Your Answer: {q['options'][user]})")
            text = f"Q{i+1}: {q['question']}\n✔ Correct: {q['options'][correct]}\n➡ {status}\n"
            tk.Label(frame, text=text, font=("Calibri", 13), bg="#f4f6f7", justify="left", wraplength=800).pack(anchor="w", padx=40, pady=5)

        tk.Label(self.root, text="🏆 Leaderboard - Top 5", font=("Verdana", 18, "bold"), bg="#f4f6f7", fg="#8e44ad").pack(pady=10)
        for i, entry in enumerate(self.get_leaderboard(), start=1):
            text = f"{i}. {entry['name']} - {entry['score']} pts ({entry['category']}, {entry['level']})"
            tk.Label(self.root, text=text, font=("Calibri", 13), bg="#f4f6f7").pack()

        tk.Button(self.root, text="🔁 Back to Home", font=self.button_font, bg="#17a2b8", fg="white", command=self.welcome_screen).pack(pady=10)
        tk.Button(self.root, text="Exit ❌", font=self.button_font, bg="#dc3545", fg="white", command=self.root.quit).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
app = StylishQuizApp(root)
root.mainloop()
