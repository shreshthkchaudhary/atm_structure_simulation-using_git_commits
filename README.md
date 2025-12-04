# ATM Structure Simulation

## Project Description

A console-based **ATM (Automated Teller Machine) Simulation** built in Python that replicates core banking operations. This project demonstrates fundamental programming concepts including functions, control flow, input validation, and state management in a practical real-world application.

## ✨ Features

- ✅ **Check Balance** - View current account balance (Initial: Rs. 1000)
- ✅ **Deposit Money** - Add funds to the account with validation (≥ Rs. 1)
- ✅ **Withdrawal** - Withdraw funds with balance verification (no overdrafts)
- ✅ **Menu Navigation** - User-friendly console-based menu system
- ✅ **Input Validation** - Prevents invalid transactions and menu choices
- ✅ **Sub-menu Navigation** - Continue transactions or exit gracefully

## 🚀 Installation & Usage

### Prerequisites
- Python 3.x installed on your system

### Steps to Run

1. **Clone the Repository**
git clone https://github.com/shreshthkchaudhary/atm_structure_simulation-using_git_commits.git
cd atm_structure_simulation-using_git_commits

2. **Run the Program**
python atm_structure_simulation.py

3. **Follow the Menu Prompts**
ATM Menu:
To Check Balance give input 1
To Deposit Amount give input 2
To do Withdrawal give input 3
To Exit give input 4

Choice option: Enter your choice (1-4):

## 📱 Example Session
ATM Menu:
To Check Balance give input 1
To Deposit Amount give input 2
To do Withdrawal give input 3
To Exit give input 4

Choice option: Enter your choice (1-4): 1
Your Current Balance is Rs1000.0

To go to Main Menu give input 1
To Exit give input 2
Choice option: Enter your choice (1-2): 2

Enter amount to Deposit :Rs500
Rs500.0 deposited successfully.
Your current balance is Rs1500.0

To go to Main Menu give input 1
To Exit give input 2
Choice option: Enter your choice (1-2): 1

## 📂 Project Structure
atm_structure_simulation/
├── .gitignore # Files to exclude from git
├── README.md # Project documentation (this file)
├── atm_structure_simulation.py # Main program file
└── docs/
├── PROJECT_OVERVIEW.md # Detailed project overview
├── DEVELOPMENT_PROCESS.md # How the project was built
└── FUTURE_IMPROVEMENTS.md # Planned enhancements

## 🛠️ Technologies Used

- **Language**: Python 3.x
- **Development Environment**: Visual Studio Code
- **Version Control**: Git & GitHub
- **Documentation**: Markdown

## 🎯 Key Concepts Demonstrated

1. **Functions**: Modular code with separate functions for each operation
2. **Input Validation**: Error handling for invalid amounts and choices
3. **State Management**: Balance tracking across multiple transactions
4. **Control Flow**: Menu navigation with if-elif-else and while loops
5. **Recursion**: Self-calling functions for invalid input handling
6. **User Interface**: Clear console-based menu system

## 📊 Sample Outputs

### Main Menu
ATM Menu:
To Check Balance give input 1
To Deposit Amount give input 2
To do Withdrawal give input 3
To Exit give input 4

### Successful Deposit
Enter amount to Deposit :Rs500
Rs500.0 deposited successfully.
Your current balance is Rs1500.0

### Withdrawal Validation
Enter amount to withdraw :Rs2000
insufficient balance
Enter amount to withdraw :Rs300
Rs300.0 withdrawn successfully.
Your current balance is Rs1200.0

## 📈 Git Development History

**5 Meaningful Commits** showing incremental development:

| # | Commit Message | Changes |
|---|----------------|---------|
| 1 | Initial commit: Add ATM program with basic menu system | Project setup + main menu |
| 2 | Add deposit functionality with balance update | Deposit feature + validation |
| 3 | Add withdrawal feature with balance validation | Withdrawal + overdraft protection |
| 4 | Add sub-menu navigation for user flow control | Continue/exit after transactions |
| 5 | Improve input validation and user messages | Enhanced error handling |
git log --oneline
7d899b4 (HEAD -> main) Initial commit: Add ATM program with basic menu system

## 🎓 Learning Outcomes

- **Programming Fundamentals**: Functions, loops, conditionals, input handling
- **Real-world Application**: Banking transaction systems
- **Professional Practices**: Version control, documentation, modular code
- **Error Handling**: Input validation and user feedback
- **Software Engineering**: Clean code structure and maintainability

## 🔮 Future Enhancements

- 🔐 **PIN Authentication** - User login security
- 💾 **Data Persistence** - Save balance to file/database
- 👥 **Multi-Account** - Support multiple users
- 📜 **Transaction History** - View past transactions
- 🖥️ **GUI Interface** - Tkinter graphical interface
- 🌐 **Web Version** - Flask/Django web application

## 📚 Academic Context

**Course**: ETCCCP105 - Computer Science Fundamentals & Career Pathways  
**Assignment**: 04 - Build & Document a Mini Project Using GitHub and VS Code  
**Institution**: KR Mangalam University, School of Engineering & Technology  
**Student**: Shreshth Kumar Chaudhary

## 📞 Support

**Repository**: https://github.com/shreshthkchaudhary/atm_structure_simulation-using_git_commits  
**Issues**: Create GitHub issue for bugs/feature requests

## 📄 License

This project is created for educational purposes as coursework submission.

---

**Built with ❤️ for learning professional software development practices**
