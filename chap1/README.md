# Chapter 1 – Git Commands with Comments

Git command 

---

```bash
# Step 1: Go to Desktop (or your desired location)
cd Desktop
# Moves your terminal to the Desktop directory where your project will be cloned.

# Step 2: Clone your GitHub repository
git clone https://github.com/ayanatiq01-arch/parallel-DC.git
# Downloads (clones) your remote GitHub repo to your computer.

# Step 3: Enter the cloned project folder
cd parallel-DC
# Opens the cloned repository so we can work inside it.

# Step 4: Create a new folder called 'chap1'
mkdir chap1
# Makes a folder named chap1 to store files related to this chapter.

# Step 5: Move into the 'chap1' folder
cd chap1
# Changes directory to the chap1 folder.

# Step 6: Create a simple text file with some content
echo "My first chapter notes" > notes.txt
# Creates a text file named notes.txt with a line of text inside.

# Step 7: Check the current Git status
git status
# Shows which files are untracked, modified, or ready to be staged.

# Step 8: Stage all new and modified files
git add .
# Adds all changes (new files and folders) to the staging area for commit.

# Step 9: Commit your staged changes
git commit -m "Created chap1 folder with notes and README file"
# Saves your staged changes locally with a descriptive message.

# Step 10: Push your commits to GitHub
git push origin main
# Uploads (pushes) your committed changes to your GitHub main branch.


<<<<<<< HEAD



---

## 📸 Output Screenshot
![Program Output](output.jpg)

---

## 🧠 Conclusion
The results show that **multiprocessing performs faster** than **multithreading** for this CPU-intensive calculation.  
This is because **processes run on separate CPU cores**, enabling true parallel execution, while **threads share the same memory space** and are limited by Python’s **Global Interpreter Lock (GIL)**.  

In summary, for **CPU-bound tasks**, multiprocessing is more efficient, whereas **multithreading** is better suited for **I/O-bound operations**.
=======
>>>>>>> 71bfd3ded938f911d1832da5bd585f03e15f8215
