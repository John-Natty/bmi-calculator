# AI-IDE Workflow Integration - Mini Project

## Project Overview

This repository was created for the **AI-IDE Workflow Integration** project.

The goal of the project was to discover how AI can be used inside a code editor to help a beginner read, write, improve, and debug code.

During this project, I tested different AI-assisted workflows:

* **VS Code** with an AI add-on
* **Cursor**, an AI-first code editor
* **ChatGPT** as a browser AI helper
* **Completion mode**
* **Chat mode**
* **Agent mode**

The final mini-project is a beginner-friendly Python app: a **BMI Calculator**.

---

## Tools Used

I used the following tools during the project:

| Tool    | Role                                                 |
| ------- | ---------------------------------------------------- |
| VS Code | Main code editor with an AI add-on                   |
| Codex   | AI assistant used inside VS Code                     |
| Cursor  | Second AI-first IDE tested for comparison            |
| ChatGPT | Browser AI helper used for explanations and guidance |
| Python  | Programming language used for the final mini-project |

---

## AI Modes Used

### 1. Completion Mode

Completion mode means the AI suggests code directly inside the editor while I type.

I used completion mode to experience automatic code suggestions in both VS Code and Cursor.

Example of use:

* I started typing small JavaScript or Python code.
* The AI suggested the next lines.
* I reviewed the suggestion before accepting it.

This helped me understand that completion is useful for writing simple code faster, but the developer still needs to check the result.

---

### 2. Chat Mode

Chat mode means asking the AI questions in a side panel or chat window.

I used chat mode to:

* ask for explanations;
* ask the AI to rewrite code in a beginner-friendly way;
* understand changes made to the code;
* debug mistakes when something was unclear.

Example of use:

I asked the AI to rewrite a JavaScript function called `checkUser` so that it was easier for a beginner to read without changing its behavior.

This showed me that chat mode is useful for learning and understanding code, not only for generating code.

---

### 3. Agent Mode

Agent mode means the AI can perform several steps on its own, such as creating folders, creating files, editing code, and reporting what it did.

I used agent mode to ask the AI to create a small project structure and generate files.

Example agent task:

```text
Please create a new folder for a beginner-friendly mini-project.
Inside it, create a README.md file and a Python file for a BMI calculator.
Explain what you created after each step.
Keep the code simple and beginner-friendly.
```

The agent helped create or organize the following project files:

```text
mini_project/
├── README.md
└── bmi_calculator.py
```

After the agent created the files, I reviewed the code, checked that the project made sense, and ran the program in the terminal.

This helped me understand that agent mode can be useful for creating a project structure, but I still need to stay in control and verify every change.

---

## Final Mini Project: BMI Calculator

The final app is a simple Python program that calculates a person's BMI.

BMI means **Body Mass Index**.

The formula is:

```text
BMI = weight / (height * height)
```

The program asks the user for:

* weight in kilograms;
* height in meters.

Then it prints:

* the BMI rounded to 2 decimals;
* a simple health category.

The program also handles invalid input, such as:

* text instead of numbers;
* zero values;
* negative values.

---

## Project Files

```text
mini_project/
├── README.md
└── bmi_calculator.py
```

### `README.md`

This file explains:

* the goal of the project;
* the AI tools used;
* the three AI modes tested;
* how the final BMI calculator works;
* how to run the program.

### `bmi_calculator.py`

This file contains the Python code for the BMI calculator.

It includes:

* a function to return the health category;
* user input for weight and height;
* BMI calculation;
* error handling for invalid input;
* beginner-friendly comments.

---

## How to Run the Program

From the project folder, run:

```bash
python3 bmi_calculator.py
```

On some systems, use:

```bash
python bmi_calculator.py
```

---

## Example

```text
Enter your weight in kilograms: 70
Enter your height in meters: 1.75
Your BMI is: 22.86
Health category: Normal weight
```

---

## What I Learned

During this project, I learned that there are several ways to use AI inside a code editor.

### VS Code with an AI Add-on

VS Code feels like a classic code editor where AI is added through an extension.

It gives more manual control, but it may require more setup.

### Cursor

Cursor feels more focused on AI from the beginning because the assistant is built directly into the editor.

It feels easier to try quickly, especially for a beginner.

### Completion

Completion is useful when I want quick suggestions while typing.

### Chat

Chat is useful when I want explanations, help, or beginner-friendly rewrites.

### Agent Mode

Agent mode is useful when I want the AI to perform a small multi-step task, such as creating folders and files.

However, I learned that I must always review what the AI creates.

---

## Important Lesson

AI can help a beginner code faster and understand things more easily, but it should not be trusted blindly.

The AI can suggest code that looks correct but changes the logic of the program.

The developer must always:

* read the code;
* test the code;
* understand the changes;
* stay in control.

The AI is an assistant, not the developer.
