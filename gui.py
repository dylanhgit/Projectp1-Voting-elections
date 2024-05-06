from tkinter import Tk, Button, Label, Entry, messagebox, StringVar, Radiobutton, IntVar, font
from models import Election

class VotingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting Application")
        self.master.geometry("400x400")  # Adjusted for new layout
        self.master.resizable(False, False)

        self.election = Election()
        self.voter_id_var = StringVar()
        self.candidate_var = IntVar(value=0)  # Variable to store candidate selection
        self.status_label = Label(master, text="", fg="red")
        self.status_label.pack(side="bottom", fill="x")

        # Custom font for titles
        title_font = font.Font(family="Helvetica", size=14, weight="bold")

        # Voter ID label and entry with custom font
        Label(master, text="Enter Voter ID:", font=title_font).pack(pady=(20, 5))
        Entry(master, textvariable=self.voter_id_var).pack(pady=10)

        # Candidate section title with custom font
        Label(master, text="Candidates", font=title_font).pack(pady=(10, 2))

        # Radio buttons for each candidate
        Radiobutton(master, text="Dylan", variable=self.candidate_var, value=1).pack(pady=2)
        Radiobutton(master, text="Josh", variable=self.candidate_var, value=2).pack(pady=2)
        Radiobutton(master, text="Will", variable=self.candidate_var, value=3).pack(pady=2)
        Radiobutton(master, text="Colby", variable=self.candidate_var, value=4).pack(pady=2)

        # Submit Vote button
        Button(master, text="Submit Vote", command=self.submit_vote).pack(pady=20)
        Button(master, text="Exit", command=self.show_results_and_exit).pack(pady=10)

    def submit_vote(self):
        voter_id = self.voter_id_var.get().strip()
        candidate_id = self.candidate_var.get()
        if not voter_id.isdigit() or len(voter_id) != 4:  # Basic validation for a 4-digit ID
            self.update_status("Invalid voter ID.", "red")
            return
        if candidate_id == 0:  # Check if a candidate has been selected
            self.update_status("No candidate selected.", "red")
            return
        if self.election.vote_for_candidate(candidate_id, voter_id):
            messagebox.showinfo("Vote Recorded", f"Your vote has been recorded for {self.election.candidates[candidate_id].name}")
            self.update_status("", "")  # Clear status after successful vote
        else:
            self.update_status("Already voted or error.", "red")

    def show_results_and_exit(self):
        votes = self.election.get_vote_summary()
        summary = "\n".join(f"{name} - {votes}" for name, votes in votes.items())
        messagebox.showinfo("Vote Summary", summary)
        self.master.quit()

    def update_status(self, message, color):
        self.status_label.config(text=message, fg=color)

def main():
    root = Tk()
    app = VotingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
